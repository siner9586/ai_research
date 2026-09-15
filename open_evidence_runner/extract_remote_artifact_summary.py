from __future__ import annotations

import argparse
import binascii
import json
import os
import re
import struct
import zipfile
import zlib
from pathlib import Path
from typing import Any

import requests

EOCD = b"PK\x05\x06"
ZIP64_LOCATOR = b"PK\x06\x07"
ZIP64_EOCD = b"PK\x06\x06"
CENTRAL = b"PK\x01\x02"
LOCAL = b"PK\x03\x04"


def get_signed_url(repository: str, artifact_id: str, token: str) -> str:
    api_url = f"https://api.github.com/repos/{repository}/actions/artifacts/{artifact_id}/zip"
    response = requests.get(
        api_url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
        allow_redirects=False,
        timeout=60,
    )
    response.raise_for_status()
    return response.headers["Location"]


def range_request(url: str, start: int, end: int) -> bytes:
    response = requests.get(
        url,
        headers={"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"},
        stream=True,
        timeout=(30, 180),
    )
    if response.status_code != 206:
        response.close()
        raise RuntimeError(f"range request was not honored: HTTP {response.status_code}")
    data = response.content
    expected = end - start + 1
    if len(data) != expected:
        raise RuntimeError(f"short range response: expected {expected}, got {len(data)}")
    return data


def remote_size(url: str) -> int:
    response = requests.get(
        url,
        headers={"Range": "bytes=0-0", "Accept-Encoding": "identity"},
        stream=True,
        timeout=(30, 120),
    )
    if response.status_code != 206:
        response.close()
        raise RuntimeError(f"server does not support byte ranges: HTTP {response.status_code}")
    content_range = response.headers.get("Content-Range", "")
    response.close()
    match = re.search(r"/(\d+)$", content_range)
    if not match:
        raise RuntimeError(f"missing total size in Content-Range: {content_range}")
    return int(match.group(1))


def parse_extra_zip64(extra: bytes, uncomp: int, comp: int, offset: int) -> tuple[int, int, int]:
    position = 0
    while position + 4 <= len(extra):
        header_id, size = struct.unpack_from("<HH", extra, position)
        position += 4
        payload = extra[position : position + size]
        position += size
        if header_id != 0x0001:
            continue
        cursor = 0
        if uncomp == 0xFFFFFFFF:
            uncomp = struct.unpack_from("<Q", payload, cursor)[0]
            cursor += 8
        if comp == 0xFFFFFFFF:
            comp = struct.unpack_from("<Q", payload, cursor)[0]
            cursor += 8
        if offset == 0xFFFFFFFF:
            offset = struct.unpack_from("<Q", payload, cursor)[0]
        return uncomp, comp, offset
    return uncomp, comp, offset


def locate_central_directory(url: str, total_size: int) -> tuple[int, int, int]:
    tail_size = min(total_size, 1024 * 1024)
    tail_start = total_size - tail_size
    tail = range_request(url, tail_start, total_size - 1)
    index = tail.rfind(EOCD)
    if index < 0:
        raise RuntimeError("ZIP EOCD record not found")
    eocd_absolute = tail_start + index
    _, _, _, _, entries, cd_size, cd_offset, _ = struct.unpack_from("<4s4H2LH", tail, index)
    if entries != 0xFFFF and cd_size != 0xFFFFFFFF and cd_offset != 0xFFFFFFFF:
        return cd_offset, cd_size, entries

    locator_absolute = eocd_absolute - 20
    locator = range_request(url, locator_absolute, eocd_absolute - 1)
    signature, _, zip64_offset, _ = struct.unpack("<4sLQL", locator)
    if signature != ZIP64_LOCATOR:
        raise RuntimeError("ZIP64 locator not found")
    zip64_header = range_request(url, zip64_offset, zip64_offset + 55)
    values = struct.unpack_from("<4sQ2H2L4Q", zip64_header, 0)
    if values[0] != ZIP64_EOCD:
        raise RuntimeError("ZIP64 EOCD signature mismatch")
    return int(values[-1]), int(values[-2]), int(values[-3])


def central_members(url: str, cd_offset: int, cd_size: int) -> list[dict[str, Any]]:
    data = range_request(url, cd_offset, cd_offset + cd_size - 1)
    members: list[dict[str, Any]] = []
    position = 0
    while position + 46 <= len(data):
        if data[position : position + 4] != CENTRAL:
            raise RuntimeError(f"central directory signature mismatch at {position}")
        flags = struct.unpack_from("<H", data, position + 8)[0]
        method = struct.unpack_from("<H", data, position + 10)[0]
        crc = struct.unpack_from("<L", data, position + 16)[0]
        comp_size = struct.unpack_from("<L", data, position + 20)[0]
        file_size = struct.unpack_from("<L", data, position + 24)[0]
        name_len = struct.unpack_from("<H", data, position + 28)[0]
        extra_len = struct.unpack_from("<H", data, position + 30)[0]
        comment_len = struct.unpack_from("<H", data, position + 32)[0]
        local_offset = struct.unpack_from("<L", data, position + 42)[0]
        name_start = position + 46
        raw_name = data[name_start : name_start + name_len]
        name = raw_name.decode("utf-8" if flags & 0x800 else "cp437")
        extra = data[name_start + name_len : name_start + name_len + extra_len]
        file_size, comp_size, local_offset = parse_extra_zip64(extra, file_size, comp_size, local_offset)
        members.append(
            {
                "filename": name,
                "method": method,
                "crc": crc,
                "compress_size": int(comp_size),
                "file_size": int(file_size),
                "local_offset": int(local_offset),
            }
        )
        position = name_start + name_len + extra_len + comment_len
    return members


def read_member(url: str, member: dict[str, Any]) -> bytes:
    local_offset = member["local_offset"]
    header = range_request(url, local_offset, local_offset + 29)
    if header[:4] != LOCAL:
        raise RuntimeError(f"local header mismatch for {member['filename']}")
    name_len = struct.unpack_from("<H", header, 26)[0]
    extra_len = struct.unpack_from("<H", header, 28)[0]
    data_start = local_offset + 30 + name_len + extra_len
    compressed = range_request(url, data_start, data_start + member["compress_size"] - 1)
    if member["method"] == 0:
        output = compressed
    elif member["method"] == 8:
        output = zlib.decompress(compressed, -15)
    else:
        raise RuntimeError(f"unsupported compression method {member['method']}")
    if len(output) != member["file_size"]:
        raise RuntimeError(f"size mismatch for {member['filename']}")
    if binascii.crc32(output) & 0xFFFFFFFF != member["crc"]:
        raise RuntimeError(f"CRC mismatch for {member['filename']}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--artifact-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    location = get_signed_url(args.repository, args.artifact_id, os.environ["GITHUB_TOKEN"])
    size = remote_size(location)
    cd_offset, cd_size, expected_entries = locate_central_directory(location, size)
    members = central_members(location, cd_offset, cd_size)
    if expected_entries and len(members) != expected_entries:
        raise RuntimeError(f"central directory entry mismatch: expected {expected_entries}, got {len(members)}")

    interesting = [
        member
        for member in members
        if member["filename"].endswith(
            (
                "crossref_all_summary.json",
                "crossref_all_search_queries.csv",
                "crossref_all_paper_master.jsonl.gz",
                "crossref_all_paper_master.csv.gz",
            )
        )
    ]
    metadata_path = args.output / "crossref_artifact_member_sizes.json"
    metadata_path.write_text(json.dumps(interesting, ensure_ascii=False, indent=2), encoding="utf-8")

    selected = [
        member
        for member in interesting
        if member["filename"].endswith(("crossref_all_summary.json", "crossref_all_search_queries.csv"))
    ]
    if len(selected) != 2:
        raise RuntimeError(f"expected summary and manifest members, found {[m['filename'] for m in selected]}")

    output_zip = args.output / "crossref-summary-only.zip"
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for member in selected:
            data = read_member(location, member)
            archive.writestr(Path(member["filename"]).name, data)
            if member["filename"].endswith("crossref_all_summary.json"):
                summary = json.loads(data)
                (args.output / "crossref_all_summary.json").write_text(
                    json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
                )
                print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps({"artifact_size": size, "selected_members": interesting}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
