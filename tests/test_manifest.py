import json
from pathlib import Path


def test_manifest_contains_required_fields():
    manifest_path = Path("custom_components/maxxisun/manifest.json")
    assert manifest_path.exists(), "manifest.json not found"

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert data["domain"] == "maxxisun"
    assert "version" in data
    assert data.get("config_flow") is True
    assert "documentation" in data
