"""Row-major blank coordinate discovery (FR-02)."""

from __future__ import annotations

from entity.constants import BLANK_VALUE, GRID_SIZE


def find_blank_coords(matrix: list[list[int]]) -> list[tuple[int, int]]:
    """Return 0-index coordinates of blank cells in row-major order.

    Args:
        matrix: Size-valid 4×4 grid with exactly two blank cells.

    Returns:
        List of ``(row, col)`` tuples for each blank, row-major ordered.
    """
    blanks: list[tuple[int, int]] = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if matrix[row][col] == BLANK_VALUE:
                blanks.append((row, col))
    return blanks
