"""Track B — D-VAL-01~06 magic square validation RED skeletons."""

from __future__ import annotations

import pytest

from entity.services.magic_square_validator import (  # noqa: F401 — RED import
    is_magic_square,
)


class TestDValMagicSquare:
    """D-VAL-01~06 — is_magic_square oracle (FR-04, I1~I5)."""

    def test_d_val_01_complete_magic_g0_is_true(self) -> None:
        """D-VAL-01: G0 (V-01) → True."""
        # Given
        # matrix = grid_g0
        # When
        # result = is_magic_square(matrix)
        pytest.fail("RED: D-VAL-01 — G0 complete magic square → True")

    def test_d_val_02_row_sum_not_m_g0_mutated_is_false(self) -> None:
        """D-VAL-02: G0 with grid[0][3]=5 (I-06) → False."""
        # Given
        # matrix = copy(grid_g0); matrix[0][3] = 5
        # When
        # result = is_magic_square(matrix)
        pytest.fail("RED: D-VAL-02 — row sum violation (I-06) → False")

    def test_d_val_03_col_sum_not_m_i07_is_false(self) -> None:
        """D-VAL-03: I-07 swap grid → False."""
        # Given
        # matrix = I-07 oracle (V-01 r0c0↔r0c1 swap)
        # When
        # result = is_magic_square(matrix)
        pytest.fail("RED: D-VAL-03 — column sum violation (I-07) → False")

    def test_d_val_04_diagonal_sum_not_m_i08_is_false(self) -> None:
        """D-VAL-04: I-08 swap grid → False."""
        # Given
        # matrix = I-08 oracle (V-01 r0c0↔r1c2 swap)
        # When
        # result = is_magic_square(matrix)
        pytest.fail("RED: D-VAL-04 — main diagonal sum violation (I-08) → False")

    def test_d_val_05_permutation_violated_i04_is_false(self) -> None:
        """D-VAL-05: I-04 duplicate grid → False."""
        # Given
        # matrix = I-04 oracle (duplicate 1 in r0/r1)
        # When
        # result = is_magic_square(matrix)
        pytest.fail("RED: D-VAL-05 — permutation violation (I-04) → False")

    def test_d_val_06_zero_in_filled_grid_is_false(self) -> None:
        """D-VAL-06: G0 with grid[3][3]=0 → False."""
        # Given
        # matrix = copy(grid_g0); matrix[3][3] = 0
        # When
        # result = is_magic_square(matrix)
        pytest.fail("RED: D-VAL-06 — zero in completed grid → False")
