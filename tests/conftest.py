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


# --- Dual-Track oracle grids G0~G3 (Report/07 §3) — RED skeleton placeholders ---
#
# @pytest.fixture
# def grid_g0() -> list[list[int]]:
#     """G0 — Report/02 V-01 complete magic square."""
#     return [
#         [1, 15, 14, 4],
#         [8, 10, 11, 5],
#         [12, 6, 7, 9],
#         [13, 3, 2, 16],
#     ]
#
# @pytest.fixture
# def grid_g1() -> list[list[int]]:
#     """G1 — two blanks; missing numbers {7, 10}."""
#     return [
#         [1, 15, 14, 4],
#         [8, 0, 11, 5],
#         [12, 6, 0, 9],
#         [13, 3, 2, 16],
#     ]
#
# @pytest.fixture
# def grid_g2() -> list[list[int]]:
#     """G2 — Step B reverse success grid (TBD)."""
#     raise NotImplementedError("RED: G2 fixture TBD")
#
# @pytest.fixture
# def grid_g3() -> list[list[int]]:
#     """G3 — unsolvable two-combination grid (TBD)."""
#     raise NotImplementedError("RED: G3 fixture TBD")
