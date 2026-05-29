"""Boundary failure response types."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from entity.oracles import (
    AC_FR_01_01_INVALID_SIZE_CODE,
    AC_FR_01_01_INVALID_SIZE_MESSAGE,
)

INVALID_SIZE_CODE: str = AC_FR_01_01_INVALID_SIZE_CODE
INVALID_SIZE_MESSAGE: str = AC_FR_01_01_INVALID_SIZE_MESSAGE


class EcbFailureSchema(BaseModel):
    """Pydantic contract for AC-FR-01-01 ECB failure payload (T-03)."""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str = Field(min_length=1)


class FailureResult(BaseModel):
    """Failure envelope returned by ECB Boundary validators (AC-FR-01-01).

    Field-compatible with Dual-Track ``FailureResponse`` (``type`` omitted for
    Wave 0 ECB contract). See ``docs/error_contracts.md``.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    code: str
    message: str
    is_failure: bool = True


HandleResult = FailureResult
