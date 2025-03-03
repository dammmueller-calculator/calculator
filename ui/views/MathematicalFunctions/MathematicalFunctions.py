import re

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication

from src.mathematical_functions.mathematical_functions import *

from ui.views.InputModule import InputModule


class MathematicalFunctions(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        uic.loadUi("ui/views/MathematicalFunctions/mathematical_functions.ui", self)

        input_widget = self.findChild(QWidget, "wi_input_module")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.tb_first_input.setVisible(False)
        self.tb_second_input.setVisible(False)

        self.last_focused_edit = None

        self.input_module.number_pressed.connect(self.update_input_line)
        self.input_module.sign_pressed.connect(self.handle_signal)

    def find_last_focused_edit(self):
        if self.combox_function_select.currentIndex() != 0:
            if QApplication.focusWidget() == self.tb_first_input:
                self.last_focused_edit = self.tb_first_input
            if QApplication.focusWidget() == self.tb_second_input:
                self.last_focused_edit = self.tb_second_input
        else:
            return

    def update_input_line(self, value):
        if self.combox_function_select.currentIndex() != 0 and self.last_focused_edit:
            text = self.last_focused_edit.toPlainText()
            self.last_focused_edit.setPlainText(text + value)
        else:
            return

    def handle_signal(self, value):
        if value == "=":
            self.handle_result_on_signal()
        if value == "C":
            self.tb_first_input.setPlainText("")
            self.tb_second_input.setPlainText("")
            self.la_result_output.setText("")
        if value == "/":
            self.update_input_line(value)

    def handle_input_on_function_select(self):
        index = self.combox_function_select.currentIndex()

        if index == 1:
            self.la_first_input.setText("Fakultät")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(False)
        elif index == 2:
            self.la_first_input.setText("Radikant")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(False)
        elif index == 3:
            self.la_first_input.setText("f(x) =")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(False)
        elif index == 4:
            self.la_first_input.setText("Unterer Grenzwert")
            self.la_second_input.setText("Oberer Grenzwert")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(True)
        elif index == 5:
            self.la_first_input.setText("Gemeiner Bruch")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(False)

        else:
            self.la_first_input.setText("")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(False)
            self.tb_second_input.setVisible(False)

    def handle_result_on_signal(self):
        result = ''
        index = self.combox_function_select.currentIndex()
        first_value = self.tb_first_input.toPlainText()
        second_value = self.tb_second_input.toPlainText()

        if index == 1:
            if not first_value:
                print("Enter value!")
                return
            elif re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            result = calculate_faculty(int(first_value))
        elif index == 2:
            if not first_value:
                print("Enter value!")
                return
            elif re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            result = calculate_square_root(int(first_value))
        elif index == 3:
            result = calculate_function()
        elif index == 4:
            if not first_value or not second_value:
                print("Enter all values")
                return
            elif re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            result = find_prime_numbers(int(first_value), int(second_value))
        elif index == 5:
            if not first_value:
                print("Enter value!")
                return
            result = convert_fraction(first_value)
        else:
            print("Please select a branch function first")
            return

        if result != '':
            self.la_result_output.setText(result[0])
            self.parent.appendHistory(result[1])
        else:
            return
