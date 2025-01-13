from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class Geometry(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        uic.loadUi("ui/views/geometry/geometry.ui", self)
        self.setStyleSheet("background-color: lightblue;")  # Temporary visual indicator
    
        self.some_method()

    def some_method(self):
        if self.parent:
            self.parent.appendHistory("Geometry view loaded")
