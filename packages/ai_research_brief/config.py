from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = REPO_ROOT / "configs"

def load_yaml(name: str) -> dict:
    path = CONFIG_DIR / name
    if not path.exists() and name.endswith(".yml"):
        path = CONFIG_DIR / name[:-4] + ".yaml"
    if not path.exists() and name.endswith(".yaml"):
        path = CONFIG_DIR / name[:-5] + ".yml"
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

def ensure_dirs() -> None:
    for p in [
        "data/raw",
        "data/processed",
        "data/content/zh/daily",
        "data/content/en/daily",
        "data/reports/qa",
        "apps/web/public/zh",
        "apps/web/public/en",
    ]:
        (REPO_ROOT / p).mkdir(parents=True, exist_ok=True)


def site_config() -> dict:
    return load_yaml("site.yaml")


def scoring_config() -> dict:
    return load_yaml("scoring.yaml")


def topics_config() -> dict:
    return load_yaml("topics.yaml")
