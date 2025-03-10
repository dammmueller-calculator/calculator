from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

from src.InputModule.InputModule import calc


class InputModule(QWidget):
    number_pressed = pyqtSignal(str)
    sign_pressed = pyqtSignal(str)
    calucated = pyqtSignal(str)
    validate_error = pyqtSignal(str)

    def __init__(self, calculate=False):
        super().__init__()
        uic.loadUi("ui/views/InputModule/InputModule.ui", self)
        self.calculate = calculate
        self.result: str = ""
        self.raw_text = ""

    def number1(self):
        self.number_pressed.emit("1")

    def number2(self):
        self.number_pressed.emit("2")

    def number3(self):
        self.number_pressed.emit("3")

    def number4(self):
        self.number_pressed.emit("4")

    def number5(self):
        self.number_pressed.emit("5")

    def number6(self):
        self.number_pressed.emit("6")

    def number7(self):
        self.number_pressed.emit("7")

    def number8(self):
        self.number_pressed.emit("8")

    def number9(self):
        self.number_pressed.emit("9")

    def number0(self):
        self.number_pressed.emit("0")

    def plus(self):
        self.sign_pressed.emit("+")

    def minus(self):
        self.sign_pressed.emit("-")

    def multiply(self):
        self.sign_pressed.emit("*")

    def divide(self):
        self.sign_pressed.emit("/")

    def equal(self):
        self.sign_pressed.emit("=")

        if self.calculate:
            try:
                self.validate(self.raw_text)
            except ValueError:
                print("Invalid input")
                self.validate_error.emit("Invalid input")
                return

            self.result = str(calc(self.raw_text))
            self.calucated.emit(self.result)

    def clear(self):
        self.sign_pressed.emit("C")

    def caret(self):
        self.sign_pressed.emit("^")

    def comma(self):
        self.sign_pressed.emit(",")

    def bracketOpen(self):
        self.sign_pressed.emit("(")

    def bracketClose(self):
        self.sign_pressed.emit(")")

    def power(self):
        self.sign_pressed.emit("^")

    def get_result(self) -> str:
        return self.result

    def hide_element(self, element: str) -> None:
        match element:
            case "^":
                self.btn_caret.setVisible(False)
            case "(":
                self.btn_bracket_open.setVisible(False)
            case ")":
                self.btn_bracket_close.setVisible(False)
            case "+":
                self.btn_plus.setVisible(False)
            case "-":
                self.btn_minus.setVisible(False)
            case "*":
                self.btn_multiply.setVisible(False)
            case "/":
                self.btn_divide.setVisible(False)
            case ",":
                self.btn_comma.setVisible(False)
            case "C":
                self.btn_c.setVisible(False)
            case _:
                raise ValueError

    def validate(self, text: str):
        valid_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        valid_signs = ["+", "-", "*", "/", "(", ")", "^", ","]
        last_char = ""

        for char in text:
            if char in valid_numbers:
                last_char = char
                continue
            if char in valid_signs:
                if last_char in valid_signs:
                    last_char = char
                continue

            self.validate_error.emit("Invalid input")
            raise ValueError
