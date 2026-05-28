"""Unit tests for User entity."""

from __future__ import annotations

import pytest

from magicsquare.entity.user import (
    DISPLAY_NAME_MAX_LENGTH,
    USER_ID_MAX_LENGTH,
    User,
    UserValidationError,
)


class TestUserCreate:
    """User.create factory tests."""

    def test_create_valid_user(self) -> None:
        # Arrange
        user_id = "learner-01"
        display_name = "QA Learner"

        # Act
        user = User.create(user_id=user_id, display_name=display_name)

        # Assert
        assert user.user_id == user_id
        assert user.display_name == display_name

    def test_create_strips_whitespace(self) -> None:
        # Arrange
        user_id = "  learner-02  "
        display_name = "  Magic Square  "

        # Act
        user = User.create(user_id=user_id, display_name=display_name)

        # Assert
        assert user.user_id == "learner-02"
        assert user.display_name == "Magic Square"

    def test_create_rejects_empty_user_id(self) -> None:
        # Arrange
        user_id = "   "
        display_name = "Valid Name"

        # Act / Assert
        with pytest.raises(UserValidationError, match="user_id"):
            User.create(user_id=user_id, display_name=display_name)

    def test_create_rejects_empty_display_name(self) -> None:
        # Arrange
        user_id = "learner-03"
        display_name = ""

        # Act / Assert
        with pytest.raises(UserValidationError, match="display_name"):
            User.create(user_id=user_id, display_name=display_name)

    def test_create_rejects_user_id_over_max_length(self) -> None:
        # Arrange
        user_id = "x" * (USER_ID_MAX_LENGTH + 1)
        display_name = "Valid"

        # Act / Assert
        with pytest.raises(UserValidationError, match="user_id"):
            User.create(user_id=user_id, display_name=display_name)

    def test_create_rejects_display_name_over_max_length(self) -> None:
        # Arrange
        user_id = "learner-04"
        display_name = "n" * (DISPLAY_NAME_MAX_LENGTH + 1)

        # Act / Assert
        with pytest.raises(UserValidationError, match="display_name"):
            User.create(user_id=user_id, display_name=display_name)


class TestUserRename:
    """User.rename tests."""

    def test_rename_returns_new_instance(self) -> None:
        # Arrange
        user = User.create(user_id="u-1", display_name="Before")

        # Act
        renamed = user.rename("After")

        # Assert
        assert renamed.display_name == "After"
        assert renamed.user_id == "u-1"
        assert user.display_name == "Before"

    def test_rename_rejects_invalid_display_name(self) -> None:
        # Arrange
        user = User.create(user_id="u-2", display_name="Valid")

        # Act / Assert
        with pytest.raises(UserValidationError, match="display_name"):
            user.rename("   ")


class TestUserImmutability:
    """Frozen User behavior tests."""

    def test_user_is_immutable(self) -> None:
        # Arrange
        user = User.create(user_id="u-3", display_name="Frozen")

        # Act / Assert
        with pytest.raises(AttributeError):
            user.display_name = "Changed"  # type: ignore[misc]
