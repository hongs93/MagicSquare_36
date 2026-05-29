"""Track A — U-OUT-01~03 output contract RED skeletons (Report/07 §4)."""

from __future__ import annotations

import pytest

from boundary.ui_boundary import UIBoundary  # noqa: F401 — RED import


class TestUOutSuccessPayload:
    """U-OUT-01~03 — success output contract (AC-FR05-03/04)."""

    def test_u_out_01_success_payload_length_six(self) -> None:
        """U-OUT-01: G1; mock execute → [2,2,7,3,3,10]; len(payload)==6."""
        # Given
        # boundary = UIBoundary()
        # matrix = grid_g1
        # mock SolvePartialMagicSquare.execute → [2, 2, 7, 3, 3, 10]
        # When
        # result = boundary.solve(matrix)
        pytest.fail("RED: U-OUT-01 — success payload length 6 (AC-FR05-03)")

    def test_u_out_02_one_indexed_coordinates(self) -> None:
        """U-OUT-02: payload [2,2,7,3,3,10]; r,c ∈ [1,4] (1-index)."""
        # Given
        # boundary = UIBoundary()
        # matrix = grid_g1
        # mock execute → [2, 2, 7, 3, 3, 10]
        # When
        # result = boundary.solve(matrix)
        pytest.fail("RED: U-OUT-02 — 1-index coordinates [2,2,7,3,3,10]")

    def test_u_out_03_exact_success_tuple_g1(self) -> None:
        """U-OUT-03: exact int[6] tuple for G1 small-first success."""
        # Given
        # boundary = UIBoundary()
        # matrix = grid_g1
        # mock execute → [2, 2, 7, 3, 3, 10]
        # When
        # result = boundary.solve(matrix)
        pytest.fail("RED: U-OUT-03 — exact success tuple [2,2,7,3,3,10] for G1")
