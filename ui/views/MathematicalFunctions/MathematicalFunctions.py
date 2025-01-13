from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication

from ui.views.InputModule import InputModule


class MathematicalFunctions(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        uic.loadUi("ui/views/percent/percent.ui", self)

        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        self.tb_first_input.setVisibility(False)
        self.tb_first_input.setVisibility(False)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

    def handle_input_on_function_select(self):
        return
