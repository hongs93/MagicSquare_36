"""Track B — D-LOC-01 blank coordinate discovery RED skeleton."""

from __future__ import annotations

import pytest

from entity.services.empty_cell_locator import (  # noqa: F401 — RED import
    find_blank_coords,
)


class TestDLocBlankCoords:
    """D-LOC-01 — row-major blank coordinates (FR-02, I6)."""

    def test_d_loc_01_blanks_row_major_g1(self) -> None:
        """D-LOC-01: G1 → 0-index [(1,1), (2,2)]."""
        # Given
        # matrix = grid_g1
        # When
        # coords = find_blank_coords(matrix)
        pytest.fail("RED: D-LOC-01 — G1 blanks row-major [(1,1), (2,2)] 0-index")
