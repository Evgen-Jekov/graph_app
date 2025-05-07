from PyQt6.QtWidgets import QMainWindow, QGridLayout, QFormLayout, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from app.gui.style.style import style

mat_evel = []

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

        self.figure = Figure(figsize=(8, 6), tight_layout=True)  # Увеличил размер
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

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

        clear = QPushButton(text='clear graph')
        clear.clicked.connect(self.clear_graph)
        
        use = QLabel(text='expressions used')
        self.mat_exp = QLabel()

        form_layout = QFormLayout()
        form_layout.addRow("X min:", self.x_min_input)
        form_layout.addRow("X max:", self.x_max_input)
        form_layout.addRow("Expression:", self.mat)
        form_layout.addRow(submit)
        form_layout.addRow(clear)

        layout.addWidget(self.canvas, 0, 0, 6, 1)
        layout.addWidget(instruction, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(form_layout, 1, 1, 6, 1)
        layout.addWidget(use, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.mat_exp, 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)

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
        mat_evel.append(f"{expr}\n")

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

        res = ''

        for i in range(len(mat_evel)):
            res += mat_evel[i]

        self.mat_exp.setText(res)

    def clear_graph(self):
        self.ax.cla()
        self.ax.set_title("Graph")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

        self.mat_exp.setText('')