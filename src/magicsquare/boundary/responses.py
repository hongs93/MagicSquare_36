"""Boundary failure response types."""

from __future__ import annotations

from dataclasses import dataclass

from entity.oracles import (
    AC_FR_01_01_INVALID_SIZE_CODE,
    AC_FR_01_01_INVALID_SIZE_MESSAGE,
)

INVALID_SIZE_CODE: str = AC_FR_01_01_INVALID_SIZE_CODE
INVALID_SIZE_MESSAGE: str = AC_FR_01_01_INVALID_SIZE_MESSAGE


@dataclass(frozen=True)
class FailureResult:
    """Failure envelope returned by Boundary validators (AC-FR-01-01)."""

    code: str
    message: str
    is_failure: bool = True


HandleResult = FailureResult
