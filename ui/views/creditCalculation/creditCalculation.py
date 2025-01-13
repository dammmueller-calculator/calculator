from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
import re
from ui.views.InputModule import InputModule
from src.creditCalculation.creditCalculation import *


class creditCalculation(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        uic.loadUi("ui/views/creditCalculation/creditCalculation.ui", self)

        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.last_focused_edit = None

        self.input_module.number_pressed.connect(self.update_input_line)
        self.input_module.sign_pressed.connect(self.handle_signal)

