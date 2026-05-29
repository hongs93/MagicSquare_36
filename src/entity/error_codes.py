"""Dual-Track boundary error code identifiers (PRD §13)."""

from __future__ import annotations

from enum import StrEnum


class DualTrackErrorCode(StrEnum):
    """Named error codes for Dual-Track ``FailureResponse.code`` (N-03)."""

    INVALID_SIZE = "E001_INVALID_SIZE"
    INVALID_BLANK_COUNT = "E002_INVALID_BLANK_COUNT"
    NULL_INPUT = "E003_NULL_INPUT"
    INVALID_RANGE = "E004_INVALID_RANGE"
    DUPLICATE_NONZERO = "E005_DUPLICATE_NONZERO"
    UNSOLVABLE = "E005_UNSOLVABLE_TWO_COMBINATIONS"


class EcbErrorCode(StrEnum):
    """Named error codes for ECB Wave 0 ``FailureResult.code`` (N-03)."""

    INVALID_SIZE = "INVALID_SIZE"
