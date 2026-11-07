from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--chunk-mib', type=int, default=75)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    chunk_size = args.chunk_mib * 1024 * 1024
    parts = []
    with args.input.open('rb') as source:
        index = 1
        while True:
            data = source.read(chunk_size)
            if not data:
                break
            part = args.output / f'{args.input.name}.part{index:03d}'
            part.write_bytes(data)
            parts.append({'file_name': part.name, 'size_bytes': len(data), 'sha256': sha256(part)})
            index += 1
    manifest = {
        'source_file_name': args.input.name,
        'source_size_bytes': args.input.stat().st_size,
        'source_sha256': sha256(args.input),
        'chunk_size_bytes': chunk_size,
        'part_count': len(parts),
        'parts': parts,
        'reassembly': 'Extract each GitHub artifact, concatenate .part files in numeric order, then verify source_sha256.',
    }
    (args.output / 'parts_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps(manifest, indent=2))
    if len(parts) < 2 or any(p['size_bytes'] > 95 * 1024 * 1024 for p in parts):
        raise SystemExit('invalid_chunk_plan')


if __name__ == '__main__':
    main()
