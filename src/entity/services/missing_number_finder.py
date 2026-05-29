"""Missing number discovery for partial magic squares (FR-03)."""

from __future__ import annotations

from entity.constants import BLANK_VALUE, VALUE_MAX, VALUE_MIN


def find_not_exist_nums(matrix: list[list[int]]) -> tuple[int, int]:
    """Return the two missing values from ``1..16`` in ascending order.

    Args:
        matrix: Size-valid 4×4 grid with non-zero values in range.

    Returns:
        Tuple ``(m_small, m_large)`` with ``m_small < m_large``.
    """
    present = {
        value
        for row in matrix
        for value in row
        if value != BLANK_VALUE
    }
    missing = [value for value in range(VALUE_MIN, VALUE_MAX + 1) if value not in present]
    return missing[0], missing[1]
