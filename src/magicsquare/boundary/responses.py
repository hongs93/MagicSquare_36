"""Boundary failure response types."""

from __future__ import annotations

from dataclasses import dataclass

INVALID_SIZE_CODE: str = "INVALID_SIZE"
INVALID_SIZE_MESSAGE: str = "Grid must be 4x4."


@dataclass(frozen=True)
class FailureResult:
    """Failure envelope returned by Boundary validators (AC-FR-01-01)."""

    code: str
    message: str
    is_failure: bool = True
