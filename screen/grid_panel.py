"""4×4 grid input panel with spin boxes for each cell."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from entity.constants import BLANK_VALUE, GRID_SIZE, VALUE_MAX, VALUE_MIN


class GridPanel(QWidget):
    """Editable 4×4 grid where ``0`` represents a blank cell."""

    def __init__(self, parent: QWidget | None = None) -> None:
        """Build the grid panel with labeled rows and columns."""
        super().__init__(parent)
        self._cells: list[list[QSpinBox]] = []
        self._build_layout()

    def _build_layout(self) -> None:
        """Create spin boxes and column/row labels."""
        outer = QVBoxLayout(self)
        grid = QGridLayout()
        grid.setSpacing(6)

        for col in range(GRID_SIZE):
            header = QLabel(str(col + 1))
            header.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(header, 0, col + 1)

        for row in range(GRID_SIZE):
            row_label = QLabel(str(row + 1))
            row_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grid.addWidget(row_label, row + 1, 0)

            row_cells: list[QSpinBox] = []
            for col in range(GRID_SIZE):
                spin = QSpinBox()
                spin.setRange(BLANK_VALUE, VALUE_MAX)
                spin.setSpecialValueText("·")
                spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
                spin.setMinimumWidth(56)
                spin.setMinimumHeight(40)
                grid.addWidget(spin, row + 1, col + 1)
                row_cells.append(spin)
            self._cells.append(row_cells)

        hint = QLabel("0 = 빈칸  ·  1~16 = 숫자")
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer.addLayout(grid)
        outer.addWidget(hint)

    def read_grid(self) -> list[list[int]]:
        """Return the current grid values as a 4×4 integer matrix.

        Returns:
            Matrix of cell values read from spin boxes.
        """
        return [[cell.value() for cell in row] for row in self._cells]

    def write_grid(self, matrix: list[list[int]]) -> None:
        """Populate spin boxes from a 4×4 matrix without triggering side effects.

        Args:
            matrix: Grid values to display.
        """
        for row_index, row in enumerate(matrix):
            for col_index, value in enumerate(row):
                self._cells[row_index][col_index].setValue(value)

    def clear_grid(self) -> None:
        """Reset every cell to blank (``0``)."""
        for row in self._cells:
            for cell in row:
                cell.setValue(BLANK_VALUE)

    def highlight_cells(self, coordinates: list[tuple[int, int]]) -> None:
        """Apply a visual highlight to the given 0-index cell coordinates.

        Args:
            coordinates: List of ``(row, col)`` positions to highlight.
        """
        self.reset_highlight()
        for row, col in coordinates:
            self._cells[row][col].setStyleSheet(
                "QSpinBox { background-color: #d4edda; font-weight: bold; }"
            )

    def reset_highlight(self) -> None:
        """Remove highlight styling from all cells."""
        for row in self._cells:
            for cell in row:
                cell.setStyleSheet("")

    def set_cell(self, row: int, col: int, value: int) -> None:
        """Set a single cell value.

        Args:
            row: 0-index row.
            col: 0-index column.
            value: Cell value in ``0`` or ``1..16``.
        """
        if VALUE_MIN <= value <= VALUE_MAX or value == BLANK_VALUE:
            self._cells[row][col].setValue(value)
