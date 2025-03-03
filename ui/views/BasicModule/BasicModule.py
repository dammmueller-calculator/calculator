from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from ui.views.InputModule import InputModule
from src.BasicCalculator.Calculator import add

class BasicModule(QWidget):

    # Global Variables
    value_list = []

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/BasicModule/BasicModule.ui", self)      

        input_widget = self.findChild(QWidget, "InputModul")
      
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.input_module.number_pressed.connect(self.update_inputLine)
        self.input_module.sign_pressed.connect(self.check_sign)

    def update_inputLine(self, value):
        #self.value_list.append(value)       
        text = self.inputLine.text()
        self.inputLine.setText(text + value)

    def check_sign(self,sign):
    # Klammer
    # Case 1: sign = "("    
        if sign == "*":
            return "*"
        elif sign == "÷":
            self.value_list.append(self.inputLine.text())
            self.value_list.append("+")
            self.inputLine.setText('')
            return "/"
        elif sign == "−":
            return "-"
        elif sign == "+":
            self.value_list.append("+")
            return "+"
        elif sign == "=":
        
            return "="
            # hier könnte jetzt eine Funktion stehen
        else:
            return sign


    # schreibe eine Funktion die die Liste auseinander nimmt und die Rechnung durchführt

    # wenn eine Opertor gedrückt wird, dann nimm Text trage in Liste Lösche Inputline

    
       

