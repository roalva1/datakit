import pytest

from datakit.records import normalize_record, select_fields


def test_normalize_record_lowercases_keys_and_strips_values():
    record = {" Sample ": "  A01  ", "DEPTH": 30}
    result = normalize_record(record)
    assert result == {" sample ": "A01", "depth": 30}


def test_normalize_record_can_preserve_keys():
    record = {"Sample": "  A01  "}
    result = normalize_record(record, lowercase_keys=False)
    assert result == {"Sample": "A01"}


def test_select_fields_returns_existing_fields():
    record = {"sample": "A01", "depth": 30, "status": "PASS"}
    result = select_fields(record, ["sample", "status"])
    assert result == {"sample": "A01", "status": "PASS"}


def test_select_fields_skips_missing_fields_by_default():
    record = {"sample": "A01"}
    result = select_fields(record, ["sample", "depth"])
    assert result == {"sample": "A01"}


def test_select_fields_strict_mode_raises_for_missing_field():
    record = {"sample": "A01"}
    with pytest.raises(KeyError):
        select_fields(record, ["sample", "depth"], strict=True)

def test_select_fields_none_values_are_included():
    record = {"sample": "A01", "depth": None, "status": "PASS"}
    result = select_fields(record, ["sample", "depth"])
    assert result == {"sample": "A01", "depth": None}


def test_select_fields_strict_allows_existing_none_value():
    record = {"sample": "A01", "depth": None}

    result = select_fields(
        record,
        ["sample", "depth"],
        strict=True,
    )

    assert result == {"sample": "A01", "depth": None}

def test_select_fields_non_strict_continues_after_missing_field():
    record = {"sample": "A01"}
    result = select_fields(record, ["depth", "sample", "status"], strict=False)
    assert result == {"sample": "A01"}


def test_select_fields_strict_reports_first_missing_field():
    record = {"sample": "A01"}
    with pytest.raises(KeyError) as exc_info:
        select_fields(record, ["sample", "depth", "status"], strict=True)
    assert exc_info.value.args == ("depth",)
