"""Boundary grid size validation (BR-01)."""

from __future__ import annotations

from entity.grid_validation import is_valid_grid_size

from magicsquare.boundary.responses import (
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    FailureResult,
)


class BoundaryValidator:
    """Validates that external grid input is 4×4 before Control/Domain work.

    Boundary layer: size-only contract (AC-FR-01-01). Control entry is
    ``magicsquare.control.Solver.handle`` — see ``docs/architecture_stacks.md``.
    """

    def validate_size(self, grid: list[list[int]] | None) -> FailureResult | None:
        """Return a size failure, or ``None`` when ``grid`` is 4×4.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is absent.

        Returns:
            FailureResult when size validation fails; ``None`` when dimensions are 4×4.
        """
        if not is_valid_grid_size(grid):
            return self._invalid_size_failure()
        return None

    def validate(self, grid: list[list[int]] | None) -> FailureResult:
        """Return a size failure when ``grid`` dimensions are not 4×4.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is absent.

        Returns:
            FailureResult when size validation fails.

        Raises:
            NotImplementedError: When dimensions are 4×4 but later rules are unimplemented.
        """
        size_failure = self.validate_size(grid)
        if size_failure is not None:
            return size_failure
        raise NotImplementedError("post-size validation rules not implemented")

    @staticmethod
    def _invalid_size_failure() -> FailureResult:
        """Build the AC-FR-01-01 INVALID_SIZE failure envelope."""
        return FailureResult(
            code=INVALID_SIZE_CODE,
            message=INVALID_SIZE_MESSAGE,
            is_failure=True,
        )
