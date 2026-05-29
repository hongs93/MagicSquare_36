"""Boundary input validation for 4×4 magic square grids."""

from __future__ import annotations

from entity.constants import (
    BLANK_VALUE,
    GRID_SIZE,
    REQUIRED_BLANK_COUNT,
    VALUE_MAX,
    VALUE_MIN,
)

from boundary.schemas import (
    DUPLICATE_NONZERO_CODE,
    DUPLICATE_NONZERO_MESSAGE,
    FailureResponse,
    INVALID_BLANK_COUNT_CODE,
    INVALID_BLANK_COUNT_MESSAGE,
    INVALID_RANGE_CODE,
    INVALID_RANGE_MESSAGE,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    NULL_INPUT_CODE,
    NULL_INPUT_MESSAGE,
)


class InputValidator:
    """Validates external grid input before Control/Domain processing."""

    def validate(self, grid: list[list[int]] | None) -> FailureResponse | None:
        """Validate grid input and return a failure envelope when invalid.

        Validation short-circuits in order: null → size → blank count →
        value range → non-zero duplicates.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is missing.

        Returns:
            ``FailureResponse`` when validation fails; ``None`` when valid.
        """
        if grid is None:
            return FailureResponse(
                code=NULL_INPUT_CODE,
                message=NULL_INPUT_MESSAGE,
            )

        if not grid or len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
            return FailureResponse(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )

        blank_count = sum(
            1 for row in grid for value in row if value == BLANK_VALUE
        )
        if blank_count != REQUIRED_BLANK_COUNT:
            return FailureResponse(
                code=INVALID_BLANK_COUNT_CODE,
                message=INVALID_BLANK_COUNT_MESSAGE,
            )

        for row in grid:
            for value in row:
                if value != BLANK_VALUE and (value < VALUE_MIN or value > VALUE_MAX):
                    return FailureResponse(
                        code=INVALID_RANGE_CODE,
                        message=INVALID_RANGE_MESSAGE,
                    )

        non_zero_values = [
            value for row in grid for value in row if value != BLANK_VALUE
        ]
        if len(non_zero_values) != len(set(non_zero_values)):
            return FailureResponse(
                code=DUPLICATE_NONZERO_CODE,
                message=DUPLICATE_NONZERO_MESSAGE,
            )

        return None
