from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

from ui.views.InputModule import InputModule
import src.informatik.decimalTo as InfoDEC
import src.informatik.hexTo as InfoHEX
import src.informatik.binaryTo as InfoBIN
import src.informatik.ternaryTo as InfoTERN
import src.informatik.octalTo as InfoOCT

class Informatik(QWidget):    
    number_pressed = pyqtSignal(str)  
    sign_pressed = pyqtSignal(str)       
  
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent 
        uic.loadUi("ui/views/Informatik/informatik.ui", self)
        inputWidget = self.findChild(QWidget, "InputModul")

        layout = QVBoxLayout()
        inputWidget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.input_module.hide_element(",") 
        self.input_module.hide_element("^")
        self.input_module.hide_element("+")
        self.input_module.hide_element("-")
        self.input_module.hide_element("*")
        self.input_module.hide_element("/")
        self.input_module.hide_element("(")
        self.input_module.hide_element(")")   
        #self.input_module.hide_element("C") #TODO

        self.input_module.number_pressed.connect(self.setText)
        self.input_module.sign_pressed.connect(self.setText)       

    def getInput(self):
        pass

    def setText(self, text):
        if text == '=':
            self.handle_number_system_change() # schau nach was eingabe ist 
            return
        valueText = self.inputString.text() + text
        self.inputString.setText(valueText)

    def handle_number_system_change(self):        
        index = self.inputBox.currentIndex()
        if index == 0:  # HEX
            self.hex()  
        elif index == 1:  # BIN
            self.binary()  
        elif index == 2:  # DEZ           
            self.decimal()   
        elif index == 3: # TERN
            self.terneray()   
        elif index == 4: # OCT
            self.octal()    

    def decimal(self):
        index = self.outputBox.currentIndex()
        if index == 0:    # HEX
            self.outputString.setText(InfoDEC.decimal_to_hex(self.inputString.text())) 
        elif index == 1:  # BIN          
            self.outputString.setText(InfoDEC.decimal_to_binary(self.inputString.text())) 
        elif index == 2:  # DEZ
            self.outputString.setText(self.inputString.text())
        elif index == 3:  # TERN
            self.outputString.setText(InfoDEC.decimal_to_ternary(self.inputString.text()))
        elif index == 4:  # OCT
            self.outputString.setText(InfoDEC.decimal_to_octal(self.inputString.text()))    

    def hex(self):
        index = self.outputBox.currentIndex()
        if index == 0:    # HEX
            self.outputString.setText(self.inputString.text())
        elif index == 1:  # BIN
            self.outputString.setText(InfoHEX.hex_to_binary(self.inputString.text()))
        elif index == 2:  # DEZ
            self.outputString.setText(InfoHEX.hex_to_decimal(self.inputString.text()))  
        elif index == 3:  # TERN
            self.outputString.setText(InfoHEX.hex_to_ternary(self.inputString.text()))
        elif index == 4:  # OCT
            self.outputString.setText(InfoHEX.hex_to_octal(self.inputString.text()))  

    def binary(self):
        index = self.outputBox.currentIndex()
        if index == 0:    # HEX
            self.outputString.setText(InfoBIN.binary_to_hex(self.inputString.text()))
        elif index == 1:  # BIN
            self.outputString.setText(self.inputString.text())
        elif index == 2:  # DEZ
            self.outputString.setText(InfoBIN.binary_to_decimal(self.inputString.text()))   
        elif index == 3:  # TERN
            self.outputString.setText(InfoBIN.binary_to_ternary(self.inputString.text()))
        elif index == 4:  # OCT
            self.outputString.setText(InfoBIN.binary_to_octal(self.inputString.text()))

    def terneray(self):
        index = self.outputBox.currentIndex()
        if index == 0:    # HEX
            self.outputString.setText(InfoTERN.ternary_to_hex(self.inputString.text()))
        elif index == 1:  # BIN
            self.outputString.setText(InfoTERN.ternary_to_binary(self.inputString.text()))
        elif index == 2:  # DEZ
            self.outputString.setText(InfoTERN.ternary_to_decimal(self.inputString.text()))
        elif index == 3:  # TERN
            self.outputString.setText(self.inputString.text())
        elif index == 4:  # OCT  
            self.outputString.setText(InfoTERN.ternary_to_octal(self.inputString.text()))

