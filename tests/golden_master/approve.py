"""Approve-pattern comparison for Golden Master regression tests."""

from __future__ import annotations

import difflib
import re
from pathlib import Path

GOLDEN_MASTER_EXPECTED_PATH = Path(__file__).resolve().parent.parent / "golden_master_expected.txt"

_SECTION_HEADER = re.compile(r"^\[(?P<section_id>[a-z][a-z0-9_]*)\]$")


def parse_golden_sections(document: str) -> dict[str, str]:
    """Split a golden master document into section blocks keyed by section id.

    Args:
        document: Full ``golden_master_expected.txt`` body.

    Returns:
        Map of section_id to block text (including header and trailing blank line).
    """
    sections: dict[str, str] = {}
    current_id: str | None = None
    current_lines: list[str] = []

    for line in document.splitlines():
        match = _SECTION_HEADER.match(line)
        if match:
            if current_id is not None:
                sections[current_id] = "\n".join(current_lines) + "\n"
            current_id = match.group("section_id")
            current_lines = [line]
        elif current_id is not None:
            current_lines.append(line)

    if current_id is not None:
        sections[current_id] = "\n".join(current_lines) + "\n"

    return sections


def _normalize_section(text: str) -> str:
    """Collapse trailing newlines to a single newline for section comparison.

    Args:
        text: Section block text.

    Returns:
        Text with exactly one trailing newline.
    """
    return text.rstrip("\n") + "\n"


def _unified_diff(expected: str, actual: str) -> str:
    """Build a unified diff string for two text blocks.

    Args:
        expected: Baseline text.
        actual: Current output text.

    Returns:
        Unified diff with ``expected`` / ``actual`` file labels.
    """
    return "\n".join(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile="expected",
            tofile="actual",
            lineterm="",
        )
    )


def approve(actual: str, expected_path: Path | None = None) -> None:
    """Compare *actual* to the golden file, or create it when missing.

    When the expected file does not exist, *actual* is written and the call
    returns without failure (bootstrap). When the file exists, a unified diff
    is emitted and ``AssertionError`` is raised on mismatch.

    Args:
        actual: Serialized golden master document to verify.
        expected_path: Override path; defaults to ``golden_master_expected.txt``.

    Raises:
        AssertionError: When content differs from the expected file.
    """
    path = expected_path or GOLDEN_MASTER_EXPECTED_PATH
    normalized = actual if actual.endswith("\n") else actual + "\n"

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(normalized, encoding="utf-8")
        return

    expected = path.read_text(encoding="utf-8")
    if expected != normalized:
        diff = _unified_diff(expected, normalized)
        raise AssertionError(
            "Golden Master mismatch. Re-run with APPROVE=1 to refresh baseline.\n"
            + diff
        )


def approve_section(
    actual: str,
    section_id: str,
    expected_path: Path | None = None,
) -> None:
    """Compare one scenario section to the golden file, or bootstrap when missing.

    When the expected file does not exist, the full golden master document is
    written from the live solver (bootstrap). When the file exists, only the
    block for *section_id* is compared via unified diff.

    Args:
        actual: Serialized section block for the scenario.
        section_id: Section header name (e.g. ``normal_success``).
        expected_path: Override path; defaults to ``golden_master_expected.txt``.

    Raises:
        AssertionError: When the section differs from the expected file.
    """
    from tests.golden_master.scenarios import build_golden_master_document

    path = expected_path or GOLDEN_MASTER_EXPECTED_PATH
    normalized = _normalize_section(actual)

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        document = build_golden_master_document()
        path.write_text(document, encoding="utf-8")
        return

    sections = parse_golden_sections(path.read_text(encoding="utf-8"))
    if section_id not in sections:
        raise AssertionError(
            f"Golden Master section [{section_id}] not found in {path}. "
            "Re-run with APPROVE=1 or regenerate via scripts/generate_golden_master.py."
        )

    expected_section = _normalize_section(sections[section_id])
    if expected_section != normalized:
        diff = _unified_diff(expected_section, normalized)
        raise AssertionError(
            f"Golden Master mismatch [{section_id}]. "
            "Re-run with APPROVE=1 to refresh baseline.\n"
            + diff
        )
