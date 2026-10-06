import json

from datakit.cli import summarize


def test_summarize_uses_default_minimum(tmp_path):
    path = tmp_path / "records.json"
    path.write_text(json.dumps([
        {"sample": "A", "depth": 5},
        {"sample": "B", "depth": 12},
        {"sample": "C", "depth": 30},
    ]))

    assert summarize(path) == {
        "total": 3,
        "passing": 2,
        "minimum_depth": 10,
    }


def test_summarize_respects_environment(monkeypatch, tmp_path):
    monkeypatch.setenv("DATAKIT_MIN_DEPTH", "20")
    path = tmp_path / "records.json"
    path.write_text(json.dumps([
        {"sample": "A", "depth": 5},
        {"sample": "B", "depth": 12},
        {"sample": "C", "depth": 30},
    ]))

    assert summarize(path) == {
        "total": 3,
        "passing": 1,
        "minimum_depth": 20,
    }
