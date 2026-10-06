from __future__ import annotations

from collections.abc import Iterable
from numbers import Real


def mean_numeric(values: Iterable[Real | None], 
                 mininum: Real | None = None) -> float | None:
    """Return the arithmetic mean of numeric values."""
    cleaned = [value for value in values if value is not None]

    if mininum is not None:
        cleaned = [value for value in cleaned if value >= mininum]

    if not cleaned:
        return None

    return float(sum(cleaned) / len(cleaned))
