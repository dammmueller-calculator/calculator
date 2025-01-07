from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from ui.views.InputModule import InputModule

class BasicModule(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/BasicModule/BasicModule.ui", self)
        ("background-color: lightblue;")  # Temporary visual indicator

        inputWidget = self.findChild(QWidget, "InputModul")
      
        layout = QVBoxLayout()
        inputWidget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.input_module.number_pressed.connect(self.update_inputLine)
        self.input_module.sign_pressed.connect(self.update_inputLine)

    def update_inputLine(self, value):
        text = self.inputLine.text()
        self.inputLine.setText(text + value)

