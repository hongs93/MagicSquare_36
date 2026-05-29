"""Magic square validation for completed 4×4 grids (FR-04)."""

from __future__ import annotations

from entity.constants import (
    BLANK_VALUE,
    GRID_SIZE,
    MAGIC_CONSTANT,
    VALUE_MAX,
    VALUE_MIN,
)


def is_magic_square(matrix: list[list[int]]) -> bool:
    """Return whether ``matrix`` is a valid completed 4×4 magic square.

    A completed grid must use each value in ``1..16`` exactly once with no
    blanks, and every row, column, and main/anti diagonal must sum to the
    magic constant.

    Args:
        matrix: 4×4 integer grid to validate.

    Returns:
        ``True`` when all magic-square rules hold; otherwise ``False``.
    """
    values = [cell for row in matrix for cell in row]
    if any(value == BLANK_VALUE for value in values):
        return False
    if len(set(values)) != len(values):
        return False
    if any(value < VALUE_MIN or value > VALUE_MAX for value in values):
        return False

    for row in matrix:
        if sum(row) != MAGIC_CONSTANT:
            return False

    for col in range(GRID_SIZE):
        if sum(matrix[row][col] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
            return False

    main_diagonal = sum(matrix[index][index] for index in range(GRID_SIZE))
    if main_diagonal != MAGIC_CONSTANT:
        return False

    anti_diagonal = sum(
        matrix[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE)
    )
    return anti_diagonal == MAGIC_CONSTANT
