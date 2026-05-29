"""Control-layer orchestration for partial magic square solving."""

from __future__ import annotations

from entity.constants import COORDINATE_MAX_INDEX, COORDINATE_MIN_INDEX
from entity.exceptions import UnsolvableDomainError
from entity.services.empty_cell_locator import find_blank_coords
from entity.services.magic_square_validator import is_magic_square
from entity.services.missing_number_finder import find_not_exist_nums


class SolvePartialMagicSquare:
    """Execute the two-combination solver use case (FR-05)."""

    def execute(self, matrix: list[list[int]]) -> list[int]:
        """Solve a contract-valid grid using small-first then reverse attempts.

        Args:
            matrix: Validated 4×4 grid with exactly two blanks.

        Returns:
            Six-element success payload ``[r1, c1, n1, r2, c2, n2]`` (1-index).

        Raises:
            UnsolvableDomainError: When both placement attempts fail.
        """
        return solution(matrix)


def solution(matrix: list[list[int]]) -> list[int]:
    """Run small-first and reverse placement attempts for a validated grid.

    Args:
        matrix: Validated 4×4 grid with exactly two blanks.

    Returns:
        Six-element success payload with 1-index coordinates.

    Raises:
        UnsolvableDomainError: When neither attempt yields a magic square.
    """
    blanks = find_blank_coords(matrix)
    blank1, blank2 = blanks[0], blanks[1]
    m_small, m_large = find_not_exist_nums(matrix)

    attempt_a = _try_combination(matrix, blank1, m_small, blank2, m_large)
    if attempt_a is not None:
        return attempt_a

    attempt_b = _try_combination(matrix, blank1, m_large, blank2, m_small)
    if attempt_b is not None:
        return attempt_b

    raise UnsolvableDomainError()


def _try_combination(
    matrix: list[list[int]],
    blank1: tuple[int, int],
    value1: int,
    blank2: tuple[int, int],
    value2: int,
) -> list[int] | None:
    """Fill two blanks and return a 1-index payload when the grid is magic.

    Args:
        matrix: Source grid (not mutated).
        blank1: First blank coordinate ``(row, col)`` (0-index).
        value1: Number to place at ``blank1``.
        blank2: Second blank coordinate ``(row, col)`` (0-index).
        value2: Number to place at ``blank2``.

    Returns:
        Success payload or ``None`` when the filled grid is not magic.
    """
    candidate = [row[:] for row in matrix]
    candidate[blank1[0]][blank1[1]] = value1
    candidate[blank2[0]][blank2[1]] = value2
    if not is_magic_square(candidate):
        return None

    r1, c1 = blank1
    r2, c2 = blank2
    payload = [r1 + 1, c1 + 1, value1, r2 + 1, c2 + 1, value2]
    if not _payload_shape_valid(payload):
        return None
    return payload


def _payload_shape_valid(payload: list[int]) -> bool:
    """Verify success payload coordinates are within the 1-index contract.

    Args:
        payload: Candidate six-element success payload.

    Returns:
        ``True`` when coordinates are in ``[1, 4]``.
    """
    coordinates = (payload[0], payload[1], payload[3], payload[4])
    return all(COORDINATE_MIN_INDEX <= coord <= COORDINATE_MAX_INDEX for coord in coordinates)
