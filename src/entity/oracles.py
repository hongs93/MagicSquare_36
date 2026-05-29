"""Frozen boundary oracles — single source for error codes and messages."""

from __future__ import annotations

# AC-FR-01-01 ECB Track (Report/06, PRD §8.1) — Wave 0 `tests/unit/boundary/`
AC_FR_01_01_INVALID_SIZE_CODE: str = "INVALID_SIZE"
AC_FR_01_01_INVALID_SIZE_MESSAGE: str = "Grid must be 4x4."

# Dual-Track FR-01 (Report/07, PRD §13) — `src/boundary/schemas.py`
DT_INVALID_SIZE_CODE: str = "E001_INVALID_SIZE"
DT_INVALID_SIZE_MESSAGE: str = "Input matrix must be 4x4."

DT_NULL_INPUT_CODE: str = "E003_NULL_INPUT"
DT_NULL_INPUT_MESSAGE: str = "Input matrix must not be null."
