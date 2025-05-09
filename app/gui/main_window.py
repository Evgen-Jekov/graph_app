from PyQt6.QtWidgets import QMainWindow, QGridLayout, QFormLayout, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from app.gui.style.style import style
from app.service.DRY import draw_graph
from app.service.service import WorkCoordinateLine
from app.service.service_abc import mat_evel
from app.service.DRY import show_message
from app.service.graph_repository import GraphWork
from app.service.service_abc import SAFE_FUNCS

work = WorkCoordinateLine()
graph = GraphWork()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('draw graph')
        self.setStyleSheet(style)

        layout = QGridLayout()
        widget = QWidget()

        self.figure = Figure(figsize=(8, 8), tight_layout=True)
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

        self.db_name = QLineEdit()
        add_db = QPushButton(text='Add to DB')
        search_db = QPushButton(text='Search by name')
        add_db.clicked.connect(self.add_db_graph)
        search_db.clicked.connect(self.search_db_graph)

        form_graph = QFormLayout()
        form_graph.addRow("X min:", self.x_min_input)
        form_graph.addRow("X max:", self.x_max_input)
        form_graph.addRow("Expression:", self.mat)
        form_graph.addRow(submit)
        form_graph.addRow(clear)

        form_add_db = QFormLayout()
        form_add_db.addRow("Enter name Graph", self.db_name)
        form_add_db.addRow(add_db)
        form_add_db.addRow(search_db)

        layout.addWidget(self.canvas, 0, 0, 5, 1)
        layout.addWidget(instruction, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(form_graph, 1, 1, 6, 1)
        layout.addLayout(form_add_db, 5, 1, 2, 2)
        layout.addWidget(use, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.mat_exp, 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


    def add_graph(self):
        error = work.add_graph(sl=self)

        if isinstance(error, str):
            show_message(text=error, type_message="Error")

    def clear_graph(self):
        draw_graph(self=self, dr=False)

        self.mat_exp.setText('')
        mat_evel.clear()

    def add_db_graph(self):
        result = " ".join(mat_evel)
        name = self.db_name.text()

        err = graph.add_to_graph(name_graph=name, graph=result)

        if isinstance(err, str):
            show_message(text=err, type_message='Error')

    def search_db_graph(self):
        try:
            name = self.db_name.text()
            result = graph.search_by_name(name_graph=name)

            tearing = result.split()
        
            x_min = int(self.x_min_input.text())
            x_max = int(self.x_max_input.text()) 

            x = np.linspace(x_min, x_max, 400)

            for expr in tearing:
                temp = expr.replace('\n', '') 

                try:
                    y = eval(temp, {"x": x, **SAFE_FUNCS, "__builtins__": {}})

                    if np.isscalar(y):
                        y = np.full_like(x, y)

                    draw_graph(self=self, dr=True, x=x, y=y)
            
                except Exception as e:
                    show_message(text=f"Error in expression: {e}", type_message="Error")
                
        except Exception as e:
            show_message(text=str(e), type_message='Error')
 