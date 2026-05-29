"""Boundary failure and response schemas."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

INVALID_SIZE_CODE: str = "INVALID_SIZE"
INVALID_SIZE_MESSAGE: str = "Grid must be 4x4."
ERROR_RESPONSE_TYPE: str = "ERROR"


class FailureResponse(BaseModel):
    """Standard failure envelope returned by Boundary validators."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    type: str
    code: str
    message: str
