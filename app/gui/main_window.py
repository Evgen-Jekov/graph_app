from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLabel, QWidget, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np

from app.gui.style.style import style

# ✅ Разрешённые функции
SAFE_FUNCS = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "arcsin": np.arcsin,
    "arccos": np.arccos,
    "arctan": np.arctan,
    "exp": np.exp,
    "log": np.log,
    "log10": np.log10,
    "sqrt": np.sqrt,
    "abs": np.abs,
    "floor": np.floor,
    "ceil": np.ceil,
    "round": np.round,
    "maximum": np.maximum,
    "minimum": np.minimum,
    "where": np.where,
    "clip": np.clip,
    "pi": np.pi,
    "e": np.e,
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('draw graph')
        self.setStyleSheet(style)

        layout = QGridLayout()
        widget = QWidget()

        self.figure = Figure(figsize=(5, 4), tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        self.ax.set_title("Graph")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True)

        instruction = QLabel(text='Enter a mathematical expression')
        self.mat = QLineEdit()
        self.x_min_input = QLineEdit("-10")
        self.x_max_input = QLineEdit("10")

        submit = QPushButton(text='graph add')
        submit.clicked.connect(self.add_graph)

        layout.addWidget(self.canvas, 0, 0, 3, 1)
        layout.addWidget(self.toolbar, 3, 0, 1, 1)
        layout.addWidget(instruction, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.mat, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("X min:"), 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.x_min_input, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("X max:"), 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.x_max_input, 5, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(submit, 6, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


    def add_graph(self):
        try:
            x_min = float(self.x_min_input.text())
            x_max = float(self.x_max_input.text())
            if x_min >= x_max:
                raise ValueError("x_min must be less than x_max")
        except ValueError as e:
            print(f"x range error: {e}")
            return

        x = np.linspace(x_min, x_max, 400)

        expr = self.mat.text()

        try:
            y = eval(expr, {"x": x, **SAFE_FUNCS, "__builtins__": {}})

            if np.isscalar(y):
                y = np.full_like(x, y)

            if y.shape != x.shape:
                raise ValueError("The expression must return an array of the same length as x.")

            self.ax.plot(x, y, label=expr)
            self.ax.set_title("Graph")
            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
            self.ax.grid(True)
            self.ax.legend()

            self.canvas.draw()
        except Exception as e:
            print(f"Error in expression: {e}")
