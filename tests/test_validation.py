from datakit.validation import required_fields_missing


def test_required_fields_missing():
    record = {"sample": "A01", "depth": 30}
    assert required_fields_missing(record, ["sample", "status", "depth"]) == ["status"]


def test_required_fields_missing_when_all_present():
    record = {"sample": "A01", "depth": 30}
    assert required_fields_missing(record, ["sample", "depth"]) == []
