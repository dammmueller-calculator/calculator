from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class InputModul(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/InputModul/InputModul.ui", self)
        ("background-color: lightblue;")  # Temporary visual indicator
