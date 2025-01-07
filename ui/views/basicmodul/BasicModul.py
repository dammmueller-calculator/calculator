from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from ui.views.InputModul import InputModul


class BasicModul(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/BasicModul/BasicModul.ui", self)
        ("background-color: lightblue;")  # Temporary visual indicator

        inputWidget = self.findChild(QWidget, "InputModul")
      
        layout = QVBoxLayout()
        inputWidget.setLayout(layout)

        self.input_modul = InputModul()
        layout.addWidget(self.input_modul)

        self.input_modul.number_pressed.connect(self.update_inputLine)
        self.input_modul.sign_pressed.connect(self.update_inputLine)

    def update_inputLine(self, value):
        text = self.inputLine.text()
        self.inputLine.setText(text + value)

