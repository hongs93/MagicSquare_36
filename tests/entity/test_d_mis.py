"""Track B — D-MIS-01 missing number discovery RED skeleton."""

from __future__ import annotations

import pytest

from entity.services.missing_number_finder import (  # noqa: F401 — RED import
    find_not_exist_nums,
)


class TestDMisMissingNumbers:
    """D-MIS-01 — missing numbers sorted ascending (FR-03, I7, I11)."""

    def test_d_mis_01_missing_numbers_sorted_g1(self) -> None:
        """D-MIS-01: G1 → (7, 10) ascending."""
        # Given
        # matrix = grid_g1
        # When
        # missing = find_not_exist_nums(matrix)
        pytest.fail("RED: D-MIS-01 — G1 missing numbers (7, 10) ascending")
