from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from pydantic import BaseModel, Field


class Record(BaseModel):
    sample: str
    depth: int = Field(ge=0)


def summarize(path: str | Path) -> dict[str, int]:
    min_depth = int(os.environ.get("DATAKIT_MIN_DEPTH", "10"))
    payload = json.loads(Path(path).read_text())
    records = [Record.model_validate(item) for item in payload]

    passing = [record for record in records if record.depth >= min_depth]
    return {
        "total": len(records),
        "passing": len(passing),
        "minimum_depth": min_depth,
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: datakit-summary <json-file>")

    summary = summarize(sys.argv[1])
    print(json.dumps(summary))
