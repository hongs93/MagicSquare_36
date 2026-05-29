"""GM-2 Golden Master approval tests for Magic Square Solver (UIBoundary)."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from tests.golden_master.approve import GOLDEN_MASTER_EXPECTED_PATH, approve_section
from tests.golden_master.scenarios import GM_SCENARIOS, GoldenScenario, format_section, run_scenario

pytestmark = pytest.mark.golden_master


@pytest.fixture
def golden_expected_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Use the repo baseline unless ``APPROVE=1`` (then write under tmp)."""
    if os.environ.get("APPROVE") == "1":
        path = tmp_path / "golden_master_expected.txt"
        monkeypatch.setattr(
            "tests.golden_master.approve.GOLDEN_MASTER_EXPECTED_PATH",
            path,
        )
        return path
    return GOLDEN_MASTER_EXPECTED_PATH


@pytest.mark.parametrize(
    "scenario",
    GM_SCENARIOS,
    ids=[scenario.gm_tc_id for scenario in GM_SCENARIOS],
)
def test_gm2_scenario(
    scenario: GoldenScenario,
    golden_expected_path: Path,
) -> None:
    """GM-2: one scenario block matches ``golden_master_expected.txt``.

    Verifies int[6] payload (row-major, 1-index, small-first / reverse fallback)
    or Boundary error contract (``FailureResponse.code``).
    """
    response = run_scenario(scenario)
    actual = format_section(scenario.section_id, scenario.matrix, response)
    approve_section(actual, scenario.section_id, expected_path=golden_expected_path)
