from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class Geometry(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/geometry/geometry.ui", self)
        self.setStyleSheet("background-color: lightblue;")  # Temporary visual indicator
