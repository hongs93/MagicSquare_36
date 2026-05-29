"""Shared pytest fixtures for MagicSquare RED/GREEN tests."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Keep ``src/`` ahead of ``tests/`` so ``boundary`` resolves to production code.
_ROOT = Path(__file__).resolve().parent.parent
_SRC = str(_ROOT / "src")
while _SRC in sys.path:
    sys.path.remove(_SRC)
sys.path.insert(0, _SRC)


from magicsquare.boundary.validator import BoundaryValidator
from magicsquare.control.solver import Solver


@pytest.fixture
def boundary_validator() -> BoundaryValidator:
    """Shared ECB BoundaryValidator for unit tests (R-04)."""
    return BoundaryValidator()


@pytest.fixture
def solver() -> Solver:
    """Shared ECB Solver with default validator (R-04, I-01)."""
    return Solver()


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
