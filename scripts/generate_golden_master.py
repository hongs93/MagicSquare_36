#!/usr/bin/env python3
"""Generate ``tests/golden_master_expected.txt`` from live solver output (GM-2)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests.golden_master.approve import GOLDEN_MASTER_EXPECTED_PATH  # noqa: E402
from tests.golden_master.scenarios import build_golden_master_document  # noqa: E402


def main() -> int:
    """Write the golden master baseline from current UIBoundary output.

    Returns:
        Process exit code (0 on success).
    """
    document = build_golden_master_document()
    GOLDEN_MASTER_EXPECTED_PATH.parent.mkdir(parents=True, exist_ok=True)
    GOLDEN_MASTER_EXPECTED_PATH.write_text(document, encoding="utf-8")
    print(f"Wrote {GOLDEN_MASTER_EXPECTED_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
