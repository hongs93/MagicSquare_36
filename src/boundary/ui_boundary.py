"""UI-facing boundary that validates input and orchestrates solving."""

from __future__ import annotations

from boundary.input_validator import InputValidator
from boundary.schemas import (
    FailureResponse,
    SolveResponse,
    SuccessResponse,
    UNSOLVABLE_CODE,
    UNSOLVABLE_MESSAGE,
)
from control.solve_partial_magic_square import SolvePartialMagicSquare
from entity.exceptions import UnsolvableDomainError


class UIBoundary:
    """Boundary adapter between PyQt UI and the control-layer solver."""

    def __init__(
        self,
        validator: InputValidator | None = None,
        solver: SolvePartialMagicSquare | None = None,
    ) -> None:
        """Initialize with injectable validator and solver for testing.

        Args:
            validator: Input contract validator; defaults to ``InputValidator``.
            solver: Partial magic square solver; defaults to production instance.
        """
        self._validator = validator or InputValidator()
        self._solver = solver or SolvePartialMagicSquare()

    def solve(self, matrix: list[list[int]] | None) -> SolveResponse:
        """Validate input and return a success or failure envelope.

        Args:
            matrix: User-supplied 4×4 grid, or ``None``.

        Returns:
            ``SuccessResponse`` with a six-element payload, or ``FailureResponse``.
        """
        failure = self._validator.validate(matrix)
        if failure is not None:
            return failure

        assert matrix is not None
        try:
            payload = self._solver.execute(matrix)
        except UnsolvableDomainError:
            return FailureResponse(
                code=UNSOLVABLE_CODE,
                message=UNSOLVABLE_MESSAGE,
            )

        return SuccessResponse(payload=payload)
