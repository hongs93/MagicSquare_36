"""Application entry point for the PyQt Magic Square GUI."""

from __future__ import annotations

import sys
from pathlib import Path


def _ensure_src_on_path() -> None:
    """Add ``src/`` to ``sys.path`` so dual-track packages resolve."""
    src_dir = Path(__file__).resolve().parents[1] / "src"
    src_path = str(src_dir)
    if src_path not in sys.path:
        sys.path.insert(0, src_path)


def main() -> int:
    """Launch the Magic Square GUI application.

    Returns:
        Process exit code from ``QApplication.exec()``.
    """
    _ensure_src_on_path()

    from PyQt6.QtWidgets import QApplication

    from screen.main_window import MainWindow

    app = QApplication(sys.argv)
    app.setApplicationName("MagicSquare")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
