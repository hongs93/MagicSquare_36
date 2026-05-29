"""Boundary grid size validation (BR-01)."""

from __future__ import annotations

from magicsquare.boundary.responses import (
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    FailureResult,
)
from magicsquare.entity.constants import GRID_SIZE


class BoundaryValidator:
    """Validates that external grid input is 4×4 before Control/Domain work."""

    def validate(self, grid: list[list[int]] | None) -> FailureResult:
        """Return a size failure when ``grid`` dimensions are not 4×4.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is absent.

        Returns:
            FailureResult when size validation fails.

        Raises:
            NotImplementedError: When dimensions are 4×4 but later rules are unimplemented.
        """
        if grid is None or not grid:
            return FailureResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
                is_failure=True,
            )
        if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
            return FailureResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
                is_failure=True,
            )
        raise NotImplementedError("size validation not implemented")
