"""Track A — U-IN-04~08 input validation RED skeletons (Report/07 §4)."""

from __future__ import annotations

import pytest

from boundary.input_validator import InputValidator  # noqa: F401 — RED import


class TestUInBlankCount:
    """U-IN-04~08 — blank count contract (AC-FR01-02)."""

    def test_u_in_04_blank_count_three_returns_e002(self) -> None:
        """U-IN-04: G1 + one extra blank (total 3) → E002."""
        # Given
        # validator = InputValidator()
        # matrix = grid_g1 with one additional 0 cell (3 blanks total)
        # When
        # result = validator.validate(matrix)
        # Then — (deferred to GREEN)
        pytest.fail("RED: U-IN-04 — blank count 3 → E002_INVALID_BLANK_COUNT")

    def test_u_in_05_negative_value_returns_e004(self) -> None:
        """U-IN-05: G1 with matrix[0][0] = -1 → E004."""
        # Given
        # validator = InputValidator()
        # matrix = copy of G1; matrix[0][0] = -1
        # When
        # result = validator.validate(matrix)
        pytest.fail("RED: U-IN-05 — negative value → E004_INVALID_RANGE")

    def test_u_in_06_value_seventeen_returns_e004(self) -> None:
        """U-IN-06 (Report/07 U-IN-05b): G1 with matrix[0][0] = 17 → E004."""
        # Given
        # validator = InputValidator()
        # matrix = copy of G1; matrix[0][0] = 17
        # When
        # result = validator.validate(matrix)
        pytest.fail("RED: U-IN-06 — value 17 → E004_INVALID_RANGE")

    def test_u_in_07_nonzero_duplicate_returns_e005(self) -> None:
        """U-IN-07 (Report/07 U-IN-06): G1 + duplicate non-zero → E005."""
        # Given
        # validator = InputValidator()
        # matrix = copy of G1 with duplicated non-zero value 5
        # When
        # result = validator.validate(matrix)
        pytest.fail("RED: U-IN-07 — non-zero duplicate → E005_DUPLICATE_NONZERO")

    def test_u_in_08_blank_count_one_returns_e002(self) -> None:
        """U-IN-08: PRD RD-04 — single blank → E002."""
        # Given
        # validator = InputValidator()
        # matrix = G0 with exactly one 0 cell
        # When
        # result = validator.validate(matrix)
        pytest.fail("RED: U-IN-08 — blank count 1 → E002_INVALID_BLANK_COUNT")
