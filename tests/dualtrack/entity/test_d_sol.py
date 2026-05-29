"""Track B — D-SOL-01~04 two-combination solver RED skeletons."""

from __future__ import annotations

import pytest

from control.solve_partial_magic_square import solution  # noqa: F401 — RED import


class TestDSolTwoCombination:
    """D-SOL-01~04 — solution() use case (FR-05, I8~I10). Domain Mock 금지."""

    def test_d_sol_01_step_a_success_g1(self) -> None:
        """D-SOL-01: G1 → [2,2,7,3,3,10] exact (small-first)."""
        # Given
        # matrix = grid_g1
        # When
        # payload = solution(matrix)
        pytest.fail("RED: D-SOL-01 — G1 Step A success [2,2,7,3,3,10]")

    def test_d_sol_02_reverse_success_g2(self) -> None:
        """D-SOL-02: G2 placeholder — Step B reverse success."""
        # Given
        # matrix = grid_g2  # TBD
        # When
        # payload = solution(matrix)
        pytest.fail("RED: D-SOL-02 — G2 TBD")

    def test_d_sol_03_unsolvable_g3_raises(self) -> None:
        """D-SOL-03: G3 → UnsolvableDomainError (both attempts fail)."""
        # Given
        # matrix = grid_g3  # TBD
        # When
        # with pytest.raises(UnsolvableDomainError):
        #     solution(matrix)
        pytest.fail("RED: D-SOL-03 — G3 both combinations fail → UnsolvableDomainError")

    def test_d_sol_04_payload_shape_one_index_g1(self) -> None:
        """D-SOL-04: G1 → len 6; coordinates in [1,4]."""
        # Given
        # matrix = grid_g1
        # When
        # payload = solution(matrix)
        pytest.fail("RED: D-SOL-04 — payload len 6, 1-index coords ∈ [1,4]")
