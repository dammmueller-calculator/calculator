from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal

class InputModul(QWidget):    
    number_pressed = pyqtSignal(str)  
    sign_pressed = pyqtSignal(str)       
  
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/InputModul/InputModul.ui", self)
        ("background-color: lightblue;")  # Temporary visual indicator
             
    def number1(self):
        self.number_pressed.emit('1')
          
    def number2(self):
        self.number_pressed.emit('2')
    
    def number3(self):
        self.number_pressed.emit('3')

    def number4(self):
        self.number_pressed.emit('4')

    def number5(self):      
        self.number_pressed.emit('5')

    def number6(self):
        self.number_pressed.emit('6')

    def number7(self):
        self.number_pressed.emit('7')

    def number8(self):    
        self.number_pressed.emit('8')

    def number9(self):
        self.number_pressed.emit('9')

    def number0(self):
        self.number_pressed.emit('0')

    def numberPlus(self):
        self.sign_pressed.emit('+')

    def numberMinus(self):
        self.sign_pressed.emit('-')

    def numberMultiply(self):
        self.sign_pressed.emit('*')

    def numberDivide(self):
        self.sign_pressed.emit('/')

        