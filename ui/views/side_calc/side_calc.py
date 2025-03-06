from PyQt6 import uic
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtCore import pyqtSignal

from ui.views.InputModule import InputModule


class SideCalc(QWidget):
    side_calc_done = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.result = None

        uic.loadUi("ui/views/BasicModule/BasicModule.ui", self)

        inputWidget = self.findChild(QWidget, "InputModul")

        layout = QVBoxLayout()
        inputWidget.setLayout(layout)

        self.input_module = InputModule(calculate=True)
        layout.addWidget(self.input_module)

        self.input_module.number_pressed.connect(self.update_inputLine)
        self.input_module.sign_pressed.connect(self.update_inputLine)
        self.input_module.calucated.connect(self.show_result)
        self.input_module.validate_error.connect(self.show_error)

    def update_raw_text(self, value):
        self.input_module.raw_text = value

    def update_inputLine(self, value):
        if value == "=":
            return
        text = self.inputLine.text()
        self.inputLine.setText(text + value)

    def show_result(self, value):
        self.result = value
        self.parent.appendHistory(self.inputLine.text() + " = " + value)
        self.inputLine.setText(value)
        
        self.side_calc_done.emit(self.result)

    def show_error(self, value):
        self.errorLine.setText(f"ERROR: {value}")
