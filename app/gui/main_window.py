from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLabel, QWidget, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from app.gui.style.style import style

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

        self.ax.set_title("Graph")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True)

        instruction = QLabel(text='Enter a mathematical expression')
        self.mat = QLineEdit()
        submit = QPushButton(text='graph add')
        submit.clicked.connect(self.add_graph)

        layout.addWidget(self.canvas, 0, 0, 3, 1)
        layout.addWidget(instruction, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.mat, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(submit, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


    def add_graph(self):
        x = np.linspace(-10, 10, 400)
        print(x)