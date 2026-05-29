"""User domain entity (ECB scaffolding — outside magic-square solve path).

Report/03 training artifact for domain entity invariants. Not wired into
``Solver``, ``UIBoundary``, or ``InputValidator``. See ``docs/architecture_stacks.md`` §5.
"""

from __future__ import annotations

from dataclasses import dataclass

USER_ID_MAX_LENGTH = 64
DISPLAY_NAME_MAX_LENGTH = 100


class UserValidationError(ValueError):
    """Raised when User domain invariants are violated."""


@dataclass(frozen=True, slots=True)
class User:
    """MagicSquare 서비스를 이용하는 사용자 도메인 엔티티.

    검증기 사용·회귀 테스트 추적 등에서 주체를 식별하는 값 객체이다.
    I/O·프레임워크에 의존하지 않는다.

    Attributes:
        user_id: 시스템 내 고유 사용자 식별자(공백 불가).
        display_name: UI·로그에 표시할 이름(공백 불가).
    """

    user_id: str
    display_name: str

    def __post_init__(self) -> None:
        """생성 직후 불변식을 검증한다."""
        self._validate_user_id(self.user_id)
        self._validate_display_name(self.display_name)
        object.__setattr__(self, "user_id", self.user_id.strip())
        object.__setattr__(self, "display_name", self.display_name.strip())

    @classmethod
    def create(cls, user_id: str, display_name: str) -> User:
        """검증 규칙을 적용해 User 인스턴스를 생성한다.

        Args:
            user_id: 고유 사용자 식별자.
            display_name: 표시 이름.

        Returns:
            검증을 통과한 User 인스턴스.

        Raises:
            UserValidationError: 식별자·표시 이름이 규칙을 위반할 때.
        """
        return cls(user_id=user_id, display_name=display_name)

    def rename(self, display_name: str) -> User:
        """표시 이름만 바꾼 새 User를 반환한다(불변).

        Args:
            display_name: 새 표시 이름.

        Returns:
            display_name이 갱신된 User.

        Raises:
            UserValidationError: 표시 이름이 규칙을 위반할 때.
        """
        return User(user_id=self.user_id, display_name=display_name)

    @staticmethod
    def _validate_user_id(user_id: str) -> None:
        """user_id 불변식을 검사한다.

        Args:
            user_id: 검사할 식별자.

        Raises:
            UserValidationError: 비어 있거나 길이 초과 시.
        """
        if not isinstance(user_id, str):
            raise UserValidationError("user_id must be a string")
        if not user_id.strip():
            raise UserValidationError("user_id must not be empty or whitespace")
        if len(user_id.strip()) > USER_ID_MAX_LENGTH:
            raise UserValidationError(
                f"user_id must be at most {USER_ID_MAX_LENGTH} characters"
            )

    @staticmethod
    def _validate_display_name(display_name: str) -> None:
        """display_name 불변식을 검사한다.

        Args:
            display_name: 검사할 표시 이름.

        Raises:
            UserValidationError: 비어 있거나 길이 초과 시.
        """
        if not isinstance(display_name, str):
            raise UserValidationError("display_name must be a string")
        if not display_name.strip():
            raise UserValidationError(
                "display_name must not be empty or whitespace"
            )
        if len(display_name.strip()) > DISPLAY_NAME_MAX_LENGTH:
            raise UserValidationError(
                "display_name must be at most "
                f"{DISPLAY_NAME_MAX_LENGTH} characters"
            )
