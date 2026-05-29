"""AC-FR-01-01, PRD §8.1 INVALID_SIZE — Control layer Domain isolation RED tests."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from magicsquare.control.solver import Solver
from tests.constants import EXPECTED_INVALID_SIZE_CODE, EXPECTED_INVALID_SIZE_MESSAGE


class TestDomainIsolation:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — resolve() 격리 검증 (AC-FR-01-05)."""

    # AC-FR-01-01 / AC-FR-01-05
    def test_none_grid_resolve_called_zero_times(self, solver: Solver) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        grid = None
        resolve_mock = MagicMock()

        # When
        with patch.object(solver, "resolve", resolve_mock):
            result = solver.handle(grid)

        # Then
        resolve_mock.assert_not_called()
        assert result.code == EXPECTED_INVALID_SIZE_CODE

    # AC-FR-01-01 / AC-FR-01-05
    def test_empty_list_resolve_called_zero_times(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        solver = Solver()
        grid: list[list[int]] = []
        resolve_mock = MagicMock()

        # When
        with patch.object(solver, "resolve", resolve_mock):
            result = solver.handle(grid)

        # Then
        resolve_mock.assert_not_called()
        assert result.code == EXPECTED_INVALID_SIZE_CODE

    # AC-FR-01-01 / AC-FR-01-05
    def test_four_empty_rows_resolve_called_zero_times(
        self,
        grid_four_rows_zero_cols: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        solver = Solver()
        grid = grid_four_rows_zero_cols
        resolve_mock = MagicMock()

        # When
        with patch.object(solver, "resolve", resolve_mock):
            result = solver.handle(grid)

        # Then
        resolve_mock.assert_not_called()
        assert result.code == EXPECTED_INVALID_SIZE_CODE

    # AC-FR-01-01 / AC-FR-01-05
    def test_3x4_matrix_resolve_called_zero_times(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        solver = Solver()
        grid = grid_3x4
        resolve_mock = MagicMock()

        # When
        with patch.object(solver, "resolve", resolve_mock):
            result = solver.handle(grid)

        # Then
        resolve_mock.assert_not_called()
        assert result.code == EXPECTED_INVALID_SIZE_CODE

    # AC-FR-01-01 / AC-FR-01-05
    def test_none_grid_handle_returns_failure_without_resolve(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        solver = Solver()
        grid = None

        # When
        with patch.object(Solver, "resolve", autospec=True) as class_resolve:
            result = solver.handle(grid)

        # Then
        class_resolve.assert_not_called()
        assert result.message == EXPECTED_INVALID_SIZE_MESSAGE
        assert result.is_failure is True
