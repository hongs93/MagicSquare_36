"""Control-layer solver orchestration (FR-05 entry point)."""

from __future__ import annotations

from magicsquare.boundary.responses import FailureResult
from magicsquare.boundary.validator import BoundaryValidator


class Solver:
    """Orchestrates validation and domain resolution for magic square grids.

    ECB Training Stack Control (AC-FR-01-01, AC-FR-01-05). Dual-Track
    production counterpart: ``control.SolvePartialMagicSquare`` (FR-05).
    See ``docs/architecture_stacks.md`` §3.
    """

    def __init__(self) -> None:
        """Initialize the solver with a boundary size validator."""
        self._validator = BoundaryValidator()

    def handle(self, grid: list[list[int]] | None) -> FailureResult:
        """Validate grid size and delegate to domain resolution when valid.

        Args:
            grid: 4×4 integer matrix, or ``None`` when input is absent.

        Returns:
            FailureResult when size validation fails.

        Raises:
            NotImplementedError: When size is valid but domain resolve is not implemented.
        """
        size_failure = self._validator.validate_size(grid)
        if size_failure is not None:
            return size_failure
        return self.resolve(grid)

    def resolve(self, grid: list[list[int]] | None) -> FailureResult:
        """Run domain resolution for a size-valid grid.

        Args:
            grid: Size-valid 4×4 integer matrix.

        Returns:
            FailureResult or success envelope (not implemented).

        Raises:
            NotImplementedError: Until FR-02~05 domain logic is implemented.
        """
        raise NotImplementedError("domain resolve not implemented")
