"""Golden Master input scenarios (GM-2 Magic Square Solver)."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

_SRC = str(Path(__file__).resolve().parents[2] / "src")
while _SRC in sys.path:
    sys.path.remove(_SRC)
sys.path.insert(0, _SRC)

from boundary.schemas import SolveResponse
from boundary.ui_boundary import UIBoundary


@dataclass(frozen=True)
class GoldenScenario:
    """One GM-2 scenario: test id, section id, matrix input, and UIBoundary solve."""

    gm_tc_id: str
    section_id: str
    matrix: list[list[int]] | None
    description: str


def _matrix_normal_success() -> list[list[int]]:
    return [
        [16, 2, 3, 13],
        [5, 11, 10, 8],
        [9, 7, 0, 12],
        [4, 14, 15, 0],
    ]


def _matrix_reverse_success() -> list[list[int]]:
    """G1 workshop grid: small-first fails, reverse succeeds."""
    return [
        [1, 15, 14, 4],
        [8, 0, 11, 5],
        [12, 6, 0, 9],
        [13, 3, 2, 16],
    ]


def _matrix_invalid_blank_count() -> list[list[int]]:
    matrix = _matrix_normal_success()
    matrix[0][0] = 0
    return matrix


def _matrix_duplicate_number() -> list[list[int]]:
    matrix = [row[:] for row in _matrix_normal_success()]
    matrix[0][1] = matrix[0][2]
    return matrix


def _matrix_no_valid_solution() -> list[list[int]]:
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 0, 12],
        [13, 14, 15, 0],
    ]


GM_SCENARIOS: tuple[GoldenScenario, ...] = (
    GoldenScenario(
        gm_tc_id="GM-TC-01",
        section_id="normal_success",
        matrix=_matrix_normal_success(),
        description="Valid partial grid; solver returns success payload.",
    ),
    GoldenScenario(
        gm_tc_id="GM-TC-02",
        section_id="reverse_success",
        matrix=_matrix_reverse_success(),
        description="G1 grid: Attempt 1 fails, Attempt 2 (reverse) succeeds.",
    ),
    GoldenScenario(
        gm_tc_id="GM-TC-03",
        section_id="invalid_blank_count",
        matrix=_matrix_invalid_blank_count(),
        description="Three blanks (0); validator rejects before solver.",
    ),
    GoldenScenario(
        gm_tc_id="GM-TC-04",
        section_id="duplicate_number",
        matrix=_matrix_duplicate_number(),
        description="Duplicate non-zero values; validator rejects.",
    ),
    GoldenScenario(
        gm_tc_id="GM-TC-05",
        section_id="no_valid_solution",
        matrix=_matrix_no_valid_solution(),
        description="Valid input; both placement attempts fail.",
    ),
)


def run_scenario(
    scenario: GoldenScenario,
    boundary: UIBoundary | None = None,
) -> SolveResponse:
    """Run UIBoundary.solve for one GM scenario.

    Args:
        scenario: Golden master scenario definition.
        boundary: Optional injectable boundary for tests.

    Returns:
        ``SolveResponse`` from ``UIBoundary.solve``.
    """
    ui = boundary or UIBoundary()
    return ui.solve(scenario.matrix)


def capture_solve_response(
    boundary: UIBoundary | None = None,
) -> dict[str, SolveResponse]:
    """Run UIBoundary.solve for every GM scenario.

    Args:
        boundary: Optional injectable boundary for tests.

    Returns:
        Map of section_id to ``SolveResponse``.
    """
    ui = boundary or UIBoundary()
    return {scenario.section_id: ui.solve(scenario.matrix) for scenario in GM_SCENARIOS}


def format_matrix(matrix: list[list[int]] | None) -> str:
    """Format a 4×4 matrix as space-separated rows for the golden file.

    Args:
        matrix: Grid rows, or ``None`` for absent input.

    Returns:
        Multi-line string with one row per line.
    """
    if matrix is None:
        return "(none)"
    return "\n".join(" ".join(str(value) for value in row) for row in matrix)


def format_payload(payload: list[int]) -> str:
    """Format success payload as a compact comma-separated list.

    Args:
        payload: Six-element 1-index success tuple.

    Returns:
        Bracketed list string, e.g. ``[3,3,6,4,4,1]``.
    """
    inner = ",".join(str(value) for value in payload)
    return f"[{inner}]"


def format_section(section_id: str, matrix: list[list[int]] | None, response: SolveResponse) -> str:
    """Serialize one scenario block for ``golden_master_expected.txt``.

    Args:
        section_id: Section header name (e.g. ``normal_success``).
        matrix: Input grid shown under ``Input:``.
        response: UIBoundary solve result.

    Returns:
        Single scenario block including trailing blank line.
    """
    lines = [f"[{section_id}]", "Input:", format_matrix(matrix)]
    if response.is_failure:
        lines.extend(["Error:", response.code])
    else:
        lines.extend(["Output:", format_payload(response.payload)])
    lines.append("")
    return "\n".join(lines)


def build_golden_master_document(
    boundary: UIBoundary | None = None,
) -> str:
    """Build the full expected golden master file contents.

    Args:
        boundary: Optional injectable boundary.

    Returns:
        Complete ``golden_master_expected.txt`` body (trailing newline).
    """
    ui = boundary or UIBoundary()
    blocks: list[str] = []
    for scenario in GM_SCENARIOS:
        response = ui.solve(scenario.matrix)
        blocks.append(format_section(scenario.section_id, scenario.matrix, response))
    return "\n".join(blocks).rstrip() + "\n"
