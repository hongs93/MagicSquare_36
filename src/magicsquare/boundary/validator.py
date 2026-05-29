"""Boundary grid size validation (BR-01)."""

from __future__ import annotations

from magicsquare.boundary.responses import (
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    FailureResult,
)


class BoundaryValidator:
    """Validates that external grid input is 4×4 before Control/Domain work."""

    def validate(self, grid: list[list[int]] | None) -> FailureResult:
        """Return a size failure when ``grid`` is missing.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is absent.

        Returns:
            FailureResult when size validation fails (e.g. ``grid is None``).

        Raises:
            NotImplementedError: For non-``None`` grids until size rules are implemented.
        """
        if grid is None:
            return FailureResult(
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
                is_failure=True,
            )
        raise NotImplementedError("size validation not implemented")
