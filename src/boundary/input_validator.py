"""Boundary input validation for 4×4 magic square grids."""

from __future__ import annotations

from typing import TYPE_CHECKING

from boundary.schemas import (
    ERROR_RESPONSE_TYPE,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    FailureResponse,
)

if TYPE_CHECKING:
    Grid = list[list[int]]


class InputValidator:
    """Validates external grid input before Control/Domain processing."""

    def validate(self, grid: list[list[int]] | None) -> FailureResponse:
        """Validate grid input and return a failure envelope when invalid.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is missing.

        Returns:
            FailureResponse when validation fails (e.g. ``grid is None``).

        Raises:
            NotImplementedError: For non-``None`` grids until size rules are implemented.
        """
        if grid is None:
            return FailureResponse(
                type=ERROR_RESPONSE_TYPE,
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError("size validation not implemented")
