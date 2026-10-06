from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def required_fields_missing(
    record: Mapping[str, Any],
    required_fields: Iterable[str],
) -> list[str]:
    """Return required field names that are missing from record."""
    return [field for field in required_fields if field not in record]
