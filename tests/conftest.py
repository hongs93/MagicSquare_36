"""Shared pytest fixtures for MagicSquare RED/GREEN tests."""

from __future__ import annotations

import pytest


@pytest.fixture
def grid_3x4() -> list[list[int]]:
    """3×4 matrix — size-invalid only; cell values are in range."""
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]


@pytest.fixture
def grid_four_rows_zero_cols() -> list[list[int]]:
    """4 rows with zero columns — column count violation."""
    return [[]] * 4
