style = """
/* ---------- Общие настройки ---------- */
QWidget {
    background-color: #2e3440;
    color: #eceff4;
    font-family: "Segoe UI", "Roboto", sans-serif;
    font-size: 14px;
}

/* ---------- Метки ---------- */
QLabel {
    font-size: 16px;
    color: #88c0d0;
    margin-bottom: 6px;
}

/* ---------- Поля ввода ---------- */
QLineEdit {
    background-color: #3b4252;
    color: #eceff4;
    border: 1px solid #4c566a;
    border-radius: 6px;
    padding: 8px;
    font-size: 14px;
}

/* При фокусе */
QLineEdit:focus {
    border: 1px solid #81a1c1;
    background-color: #434c5e;
}

/* ---------- Кнопки ---------- */
QPushButton {
    background-color: #5e81ac;
    color: #eceff4;
    border: none;
    padding: 10px 18px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #81a1c1;
}

QPushButton:pressed {
    background-color: #4c566a;
}

/* ---------- Область графика ---------- */
FigureCanvas {
    background-color: #3b4252;
    border: 2px solid #4c566a;
    border-radius: 8px;
    padding: 4px;
}

/* ---------- Scrollable элементы (если будут) ---------- */
QScrollBar:vertical,
QScrollBar:horizontal {
    background: #2e3440;
    border: none;
    width: 8px;
}

QScrollBar::handle {
    background: #81a1c1;
    border-radius: 4px;
}

QScrollBar::handle:hover {
    background: #88c0d0;
}
"""