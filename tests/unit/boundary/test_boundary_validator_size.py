"""AC-FR-01-01, PRD §8.1 INVALID_SIZE — Boundary size validation RED tests."""

from __future__ import annotations

from magicsquare.boundary.responses import EcbFailureSchema, FailureResult
from magicsquare.boundary.validator import BoundaryValidator
from tests.constants import EXPECTED_INVALID_SIZE_CODE, EXPECTED_INVALID_SIZE_MESSAGE


class TestNormalFailureReturn:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 정상 실패 반환."""

    # AC-FR-01-01
    def test_none_grid_returns_failure_invalid_size_code(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE

    # AC-FR-01-01
    def test_none_grid_returns_failure_invalid_size_message(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert result.message == EXPECTED_INVALID_SIZE_MESSAGE

    # AC-FR-01-01
    def test_none_grid_returns_result_without_exception(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert isinstance(result, FailureResult)
        assert result.is_failure is True

    # AC-FR-01-01
    def test_none_grid_failure_has_code_attribute(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert hasattr(result, "code")
        assert isinstance(result.code, str)

    # AC-FR-01-01
    def test_none_grid_failure_has_message_attribute(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert hasattr(result, "message")
        assert isinstance(result.message, str)


class TestBoundaryValues:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 경계값."""

    # AC-FR-01-01
    def test_empty_list_returns_invalid_size_failure(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid: list[list[int]] = []

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.message == EXPECTED_INVALID_SIZE_MESSAGE

    # AC-FR-01-01
    def test_four_empty_rows_returns_invalid_size_failure(
        self,
        grid_four_rows_zero_cols: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = grid_four_rows_zero_cols

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.message == EXPECTED_INVALID_SIZE_MESSAGE

    # AC-FR-01-01
    def test_3x4_matrix_returns_invalid_size_failure(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = grid_3x4

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.message == EXPECTED_INVALID_SIZE_MESSAGE

    # AC-FR-01-01
    def test_empty_list_failure_code_is_invalid_size(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid: list[list[int]] = []

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == "INVALID_SIZE"

    # AC-FR-01-01
    def test_3x4_matrix_failure_message_is_exact(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = grid_3x4

        # When
        result = validator.validate(grid)

        # Then
        assert result.message == "Grid must be 4x4."


class TestMessageIdentity:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 메시지 동일성."""

    # AC-FR-01-01
    def test_none_grid_message_matches_prd_exactly_char_by_char(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None
        expected = "Grid must be 4x4."

        # When
        result = validator.validate(grid)

        # Then
        assert result.message == expected
        assert list(result.message) == list(expected)

    # AC-FR-01-01
    def test_invalid_size_message_character_count(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None
        expected = "Grid must be 4x4."

        # When
        result = validator.validate(grid)

        # Then
        assert len(result.message) == len(expected)

    # AC-FR-01-01
    def test_invalid_size_message_starts_with_grid(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert result.message.startswith("Grid")

    # AC-FR-01-01
    def test_invalid_size_message_ends_with_period(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert result.message.endswith(".")

    # AC-FR-01-01
    def test_invalid_size_message_no_extra_whitespace(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert result.message == result.message.strip()
        assert "  " not in result.message


class TestFailureResponseType:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 실패 결과 구조체."""

    # AC-FR-01-01
    def test_none_grid_returns_failure_result_type(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert isinstance(result, FailureResult)

    # AC-FR-01-01
    def test_failure_result_matches_pydantic_schema(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)
        parsed = EcbFailureSchema.model_validate(
            {"code": result.code, "message": result.message},
        )

        # Then
        assert parsed.code == EXPECTED_INVALID_SIZE_CODE
        assert parsed.message == EXPECTED_INVALID_SIZE_MESSAGE

    # AC-FR-01-01
    def test_empty_list_returns_failure_result_type(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid: list[list[int]] = []

        # When
        result = validator.validate(grid)

        # Then
        assert isinstance(result, FailureResult)

    # AC-FR-01-01
    def test_four_empty_rows_returns_failure_result_type(
        self,
        grid_four_rows_zero_cols: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = grid_four_rows_zero_cols

        # When
        result = validator.validate(grid)

        # Then
        assert isinstance(result, FailureResult)

    # AC-FR-01-01
    def test_3x4_matrix_returns_failure_result_type(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # Given
        validator = BoundaryValidator()
        grid = grid_3x4

        # When
        result = validator.validate(grid)

        # Then
        assert isinstance(result, FailureResult)


class TestAcFr0101ScopeRestriction:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 범위 제한 (AC-FR-01-02~05, FR-02~05 제외)."""

    OUT_OF_SCOPE_CODES: tuple[str, ...] = (
        "INVALID_BLANK_COUNT",
        "INVALID_RANGE",
        "DUPLICATE_NONZERO",
        "UNSOLVABLE_TWO_COMBINATIONS",
    )

    # AC-FR-01-01
    def test_3x4_failure_code_is_not_invalid_blank_count(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — AC-FR-01-02 범위 제외."""
        # Given
        validator = BoundaryValidator()
        grid = grid_3x4

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.code != "INVALID_BLANK_COUNT"

    # AC-FR-01-01
    def test_3x4_failure_code_is_not_invalid_range(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — AC-FR-01-03 범위 제외."""
        # Given
        validator = BoundaryValidator()
        grid = grid_3x4

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.code != "INVALID_RANGE"

    # AC-FR-01-01
    def test_3x4_failure_code_is_not_duplicate_nonzero(
        self,
        grid_3x4: list[list[int]],
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — AC-FR-01-04 범위 제외."""
        # Given
        validator = BoundaryValidator()
        grid = grid_3x4

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.code != "DUPLICATE_NONZERO"

    # AC-FR-01-01
    def test_none_grid_failure_code_not_in_out_of_scope_set(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — FR-02~05 오류 코드 제외."""
        # Given
        validator = BoundaryValidator()
        grid = None

        # When
        result = validator.validate(grid)

        # Then
        assert result.code == EXPECTED_INVALID_SIZE_CODE
        assert result.code not in self.OUT_OF_SCOPE_CODES

    # AC-FR-01-01
    def test_size_only_fixtures_never_use_valid_4x4_contract(self) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 정상 4×4 입력 미포함."""
        # Given — AC-FR-01-01 size-invalid fixtures only (no FR-02~05 valid grid)
        size_invalid_grids: list[list[list[int]] | None] = [
            None,
            [],
            [[]] * 4,
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        ]
        validator = BoundaryValidator()

        # When / Then — every fixture must fail with INVALID_SIZE, not success
        for grid in size_invalid_grids:
            result = validator.validate(grid)
            assert result.code == EXPECTED_INVALID_SIZE_CODE
            assert result.is_failure is True
