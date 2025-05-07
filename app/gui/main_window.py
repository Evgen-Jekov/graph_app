from PyQt6.QtWidgets import QMainWindow, QGridLayout, QFormLayout, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from app.gui.style.style import style
from app.service.DRY import draw_graph
from app.service.service import WorkGraph
from app.service.service_abc import mat_evel

work = WorkGraph()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('draw graph')
        self.setStyleSheet(style)

        layout = QGridLayout()
        widget = QWidget()

        self.figure = Figure(figsize=(8, 6), tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        draw_graph(self=self, dr=False)

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
        work.add_graph(sl=self)

    def clear_graph(self):
        draw_graph(self=self, dr=False)

        self.mat_exp.setText('')
        mat_evel.clear()