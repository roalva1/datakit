from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def normalize_record(
    record: Mapping[str, Any],
    *,
    lowercase_keys: bool = True,
    strip_strings: bool = True,
) -> dict[str, Any]:
    """Return a normalized copy of record."""
    normalized: dict[str, Any] = {}

    for key, value in record.items():
        out_key = key.lower() if lowercase_keys else key

        if strip_strings and isinstance(value, str):
            value = value.strip()

        normalized[out_key] = value

    return normalized


def select_fields(
    record: Mapping[str, Any],
    fields: Iterable[str],
    *,
    strict: bool = False,
) -> dict[str, Any]:
    """Return the requested fields from record."""
    selected: dict[str, Any] = {}

    for field in fields:
        value = record.get(field)
        if value is None:
            if strict:
                raise KeyError(field)
            continue

        selected[field] = value

    return selected
