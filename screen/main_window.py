"""Main application window for the Magic Square solver."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCloseEvent, QFont
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from boundary.ui_boundary import UIBoundary
from entity.constants import MAGIC_CONSTANT
from screen.grid_panel import GridPanel

SAMPLE_G1: list[list[int]] = [
    [1, 15, 14, 4],
    [8, 0, 11, 5],
    [12, 6, 0, 9],
    [13, 3, 2, 16],
]


class MainWindow(QMainWindow):
    """Primary window: grid editor, solve action, and result display."""

    def __init__(self) -> None:
        """Initialize UI components and wire the boundary solver."""
        super().__init__()
        self._boundary = UIBoundary()
        self._grid = GridPanel()
        self._result_label = QLabel("격자를 입력한 뒤 「풀이」를 누르세요.")
        self._result_label.setWordWrap(True)
        self._result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._build_ui()

    def _build_ui(self) -> None:
        """Lay out grid, controls, and status area."""
        self.setWindowTitle("4×4 Magic Square Solver")
        self.setMinimumSize(520, 560)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setSpacing(16)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("4×4 마방진 풀이기")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel(f"행·열·대각선 합 = {MAGIC_CONSTANT}  ·  빈칸 2개")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        layout.addWidget(self._grid, alignment=Qt.AlignmentFlag.AlignCenter)

        button_row = QHBoxLayout()
        solve_button = QPushButton("풀이")
        solve_button.setMinimumHeight(36)
        solve_button.clicked.connect(self._on_solve)
        button_row.addWidget(solve_button)

        sample_button = QPushButton("샘플 (G1)")
        sample_button.setMinimumHeight(36)
        sample_button.clicked.connect(self._on_load_sample)
        button_row.addWidget(sample_button)

        clear_button = QPushButton("초기화")
        clear_button.setMinimumHeight(36)
        clear_button.clicked.connect(self._on_clear)
        button_row.addWidget(clear_button)
        layout.addLayout(button_row)

        result_frame = QFrame()
        result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        result_layout = QVBoxLayout(result_frame)
        result_layout.addWidget(self._result_label)
        layout.addWidget(result_frame)

    def _on_solve(self) -> None:
        """Read grid, invoke boundary solver, and display the outcome."""
        self._grid.reset_highlight()
        matrix = self._grid.read_grid()
        result = self._boundary.solve(matrix)

        if result.is_failure:
            self._result_label.setText(f"❌ {result.code}\n{result.message}")
            self._result_label.setStyleSheet("color: #c0392b;")
            return

        payload = result.payload
        r1, c1, n1, r2, c2, n2 = payload
        self._result_label.setStyleSheet("color: #1e7e34;")
        self._result_label.setText(
            "✅ 풀이 성공!\n"
            f"빈칸 ({r1},{c1}) ← {n1}   ·   빈칸 ({r2},{c2}) ← {n2}\n"
            f"payload = {payload}"
        )
        self._grid.highlight_cells([(r1 - 1, c1 - 1), (r2 - 1, c2 - 1)])
        self._grid.set_cell(r1 - 1, c1 - 1, n1)
        self._grid.set_cell(r2 - 1, c2 - 1, n2)

    def _on_load_sample(self) -> None:
        """Load the workshop G1 sample grid."""
        self._grid.reset_highlight()
        self._grid.write_grid(SAMPLE_G1)
        self._result_label.setStyleSheet("")
        self._result_label.setText("G1 샘플 격자를 불러왔습니다. 「풀이」를 누르세요.")

    def _on_clear(self) -> None:
        """Clear the grid and reset the status message."""
        self._grid.reset_highlight()
        self._grid.clear_grid()
        self._result_label.setStyleSheet("")
        self._result_label.setText("격자를 입력한 뒤 「풀이」를 누르세요.")

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802
        """Confirm exit when the user closes the window."""
        reply = QMessageBox.question(
            self,
            "종료",
            "프로그램을 종료하시겠습니까?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
