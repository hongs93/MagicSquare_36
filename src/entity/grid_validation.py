"""Shared grid dimension checks for Boundary validators."""

from __future__ import annotations

from entity.constants import GRID_SIZE


def is_valid_grid_size(grid: list[list[int]] | None) -> bool:
    """Return ``True`` when ``grid`` is a 4×4 matrix.

    Args:
        grid: Candidate grid; ``None`` and empty lists are not valid sizes.

    Returns:
        ``True`` if row and column counts equal ``GRID_SIZE``; otherwise ``False``.
    """
    if grid is None or not grid:
        return False
    return len(grid) == GRID_SIZE and all(len(row) == GRID_SIZE for row in grid)
