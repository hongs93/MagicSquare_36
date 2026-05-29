"""Domain-layer exceptions for unsolvable magic square combinations."""

from __future__ import annotations


class UnsolvableDomainError(Exception):
    """Raised when both small-first and reverse placement attempts fail."""

    def __init__(self, message: str = "No valid magic square from two fixed attempts.") -> None:
        """Initialize with a descriptive message.

        Args:
            message: Human-readable failure reason.
        """
        super().__init__(message)
        self.message = message
