"""Boundary failure and response schemas."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from entity.oracles import (
    DT_INVALID_SIZE_CODE,
    DT_INVALID_SIZE_MESSAGE,
    DT_NULL_INPUT_CODE,
    DT_NULL_INPUT_MESSAGE,
)

ERROR_RESPONSE_TYPE: str = "ERROR"
SUCCESS_RESPONSE_TYPE: str = "SUCCESS"

NULL_INPUT_CODE: str = DT_NULL_INPUT_CODE
NULL_INPUT_MESSAGE: str = DT_NULL_INPUT_MESSAGE

INVALID_SIZE_CODE: str = DT_INVALID_SIZE_CODE
INVALID_SIZE_MESSAGE: str = DT_INVALID_SIZE_MESSAGE

INVALID_BLANK_COUNT_CODE: str = "E002_INVALID_BLANK_COUNT"
INVALID_BLANK_COUNT_MESSAGE: str = "Exactly two blanks (0) are required."

INVALID_RANGE_CODE: str = "E004_INVALID_RANGE"
INVALID_RANGE_MESSAGE: str = "Values must be 0 or 1..16."

DUPLICATE_NONZERO_CODE: str = "E005_DUPLICATE_NONZERO"
DUPLICATE_NONZERO_MESSAGE: str = "Non-zero values must be unique."

UNSOLVABLE_CODE: str = "E005_UNSOLVABLE_TWO_COMBINATIONS"
UNSOLVABLE_MESSAGE: str = "No valid magic square from two fixed attempts."


class FailureResponse(BaseModel):
    """Standard failure envelope returned by Dual-Track Boundary validators."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    type: Literal["ERROR"] = ERROR_RESPONSE_TYPE
    code: str
    message: str
    is_failure: bool = True


class SuccessResponse(BaseModel):
    """Standard success envelope returned by UIBoundary."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    type: Literal["SUCCESS"] = SUCCESS_RESPONSE_TYPE
    payload: list[int] = Field(min_length=6, max_length=6)
    is_failure: bool = False


SolveResponse = FailureResponse | SuccessResponse
