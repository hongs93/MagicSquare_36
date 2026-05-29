"""Frozen boundary oracles — single source for error codes and messages."""

from __future__ import annotations

from entity.error_codes import DualTrackErrorCode, EcbErrorCode

# AC-FR-01-01 ECB Track (Report/06, PRD §8.1) — Wave 0 `tests/unit/boundary/`
AC_FR_01_01_INVALID_SIZE_CODE: str = EcbErrorCode.INVALID_SIZE
AC_FR_01_01_INVALID_SIZE_MESSAGE: str = "Grid must be 4x4."

# Dual-Track FR-01 (Report/07, PRD §13) — `src/boundary/schemas.py`
DT_INVALID_SIZE_CODE: str = DualTrackErrorCode.INVALID_SIZE
DT_INVALID_SIZE_MESSAGE: str = "Input matrix must be 4x4."

DT_NULL_INPUT_CODE: str = DualTrackErrorCode.NULL_INPUT
DT_NULL_INPUT_MESSAGE: str = "Input matrix must not be null."
