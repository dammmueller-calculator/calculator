from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
import re
from ui.views.InputModule import InputModule
from src.percent.percent import *


class Percent(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        uic.loadUi("ui/views/percent/percent.ui", self)

        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.tb_first_input.setVisible(False)
        self.tb_second_input.setVisible(False)

        self.last_focused_edit = None

        self.input_module.number_pressed.connect(self.update_input_line)
        self.input_module.sign_pressed.connect(self.handle_signal)

    def find_last_selected_text_edit(self):
        if self.combox_branch_function_select.currentIndex() != 0:
            if QApplication.focusWidget() == self.tb_first_input:
                print("first")
                self.last_focused_edit = self.tb_first_input
            if QApplication.focusWidget() == self.tb_second_input:
                print("second")
                self.last_focused_edit = self.tb_second_input
        else:
            return

    def update_input_line(self, value):
        if self.combox_branch_function_select.currentIndex() != 0 and self.last_focused_edit:
            text = self.last_focused_edit.text()
            self.last_focused_edit.setText(text + value)
        else:
            return

    def handle_signal(self, value):
        if value == "=":
            self.handle_result_on_signal()
        if value == "C":
            self.tb_first_input.setText("")
            self.tb_second_input.setText("")
            self.la_result_output.setText("")
        if value == "," and self.last_focused_edit.text().find(".") == -1:
            self.update_input_line(".")

    def handle_labels_on_select_change(self):
        index = self.combox_branch_function_select.currentIndex()
        if (index == 1) or (index == 2) or (index == 3):
            self.la_first_input.setText("Grundwert")
            self.la_second_input.setText("Prozentsatz")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(True)
        elif index == 4:
            self.la_first_input.setText("Grundwert")
            self.la_second_input.setText("Prozentwert")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(True)
        elif index == 5:
            self.la_first_input.setText("Nettopreis")
            self.la_second_input.setText("Steuersatz")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(True)
        elif index == 6:
            self.la_first_input.setText("Bruttopreis")
            self.la_second_input.setText("Steuersatz")
            self.tb_first_input.setVisible(True)
            self.tb_second_input.setVisible(True)
        else:
            self.la_first_input.setText("")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(False)
            self.tb_second_input.setVisible(False)

        self.tb_first_input.clear()
        self.tb_second_input.clear()

    def handle_result_on_signal(self):
        result = ''
        index = self.combox_branch_function_select.currentIndex()
        first_value = self.tb_first_input.text()
        second_value = self.tb_second_input.text()

        if re.search('^-.*$', second_value):
            print("Don't use negative percentages")
            return
        if not second_value or not first_value:
            print("Please enter all values")
            return

        if index == 1:
            result = add_percentage(float(first_value), float(second_value))
        elif index == 2:
            result = subtract_percentage(float(first_value), float(second_value))
        elif index == 3:
            result = percent_of(float(first_value), float(second_value))
        elif index == 4:
            result = percentage(float(first_value), float(second_value))
        elif index == 5:
            if re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            result = gross_of_net(float(first_value), float(second_value))
        elif index == 6:
            if re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            result = net_of_gross(float(first_value), float(second_value))
        else:
            print("Please select a branch function first")
            return

        if result != '':
            self.la_result_output.setText(result[0])
            self.parent.appendHistory(result[1])
        else:
            return
