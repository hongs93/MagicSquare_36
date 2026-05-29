"""Track A — U-FLOW-02 flow isolation RED skeletons (Report/07 §4, extended)."""

from __future__ import annotations

import pytest

from boundary.ui_boundary import UIBoundary  # noqa: F401 — RED import


class TestUFlowExecuteIsolation:
    """U-FLOW-02 — invalid input must not call SolvePartialMagicSquare.execute."""

    def test_u_flow_02_null_matrix_execute_not_called(self) -> None:
        """U-FLOW-02a: matrix=null; execute spy call_count==0 + E003."""
        # Given
        # boundary = UIBoundary()
        # matrix = None
        # spy/mock SolvePartialMagicSquare.execute
        # When
        # result = boundary.solve(matrix)
        # Then — spy call_count == 0 (deferred)
        pytest.fail("RED: U-FLOW-02 — null input → execute 0 calls + failure envelope")

    def test_u_flow_02_invalid_size_execute_not_called(self) -> None:
        """U-FLOW-02b: 3×4 matrix; execute spy call_count==0 + E001."""
        # Given
        # boundary = UIBoundary()
        # matrix = grid_3x4  # from tests/conftest.py
        # spy/mock SolvePartialMagicSquare.execute
        # When
        # result = boundary.solve(matrix)
        pytest.fail("RED: U-FLOW-02 — size-invalid → execute 0 calls + E001")

    def test_u_flow_02_blank_count_invalid_execute_not_called(self) -> None:
        """U-FLOW-02c: G0 (0 blanks); execute spy call_count==0 + E002."""
        # Given
        # boundary = UIBoundary()
        # matrix = grid_g0  # no blanks
        # spy/mock SolvePartialMagicSquare.execute
        # When
        # result = boundary.solve(matrix)
        pytest.fail("RED: U-FLOW-02 — blank-invalid → execute 0 calls + E002")
