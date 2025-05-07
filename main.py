from PyQt6.QtWidgets import QApplication

from app.gui.main_window import MainWindow
from app.db.get_db import base, engine
from app.db.model import Graph


if __name__ == "__main__":
    app = QApplication([])

    base.metadata.create_all(bind=engine)

    window = MainWindow()

    app.exec()