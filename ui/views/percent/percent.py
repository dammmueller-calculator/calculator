from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
import re
from ui.views.InputModul import InputModul
from src.percent.percent import *


class Percent(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/percent/percent.ui", self)
        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)
        self.input_module = InputModul()
        layout.addWidget(self.input_module)
        # self.inputModule.number_pressed.connect()

    def handle_labels_on_select_change(self):
        index = self.combox_branch_function_select.currentIndex()
        if (index == 1) or (index == 2) or (index == 3):
            self.la_first_input.setText("Grundwert")
            self.la_second_input.setText("Prozentsatz")
        elif index == 4:
            self.la_first_input.setText("Grundwert")
            self.la_second_input.setText("Prozentwert")
        elif index == 5:
            self.la_first_input.setText("Nettopreis")
            self.la_second_input.setText("Steuersatz")
        elif index == 6:
            self.la_first_input.setText("Bruttopreis")
            self.la_second_input.setText("Steuersatz")
        else:
            self.la_first_input.setText("")
            self.la_second_input.setText("")

    def handle_result_on_signal(self):
        index = self.combox_branch_function_select.currentIndex()
        first_value = self.tb_first_input.toPlainText()
        second_value = self.tb_second_input.toPlainText()

        if re.search('^-.*$', second_value):
            print("Don't use negative percentages")
            return
        if not second_value or not first_value:
            print("Please enter all values")
            return

        if index == 1:
            self.la_result_output.setText(add_percentage(float(first_value), float(second_value))[0])
        elif index == 2:
            self.la_result_output.setText(subtract_percentage(float(first_value), float(second_value))[0])
        elif index == 3:
            self.la_result_output.setText(percent_of(float(first_value), float(second_value))[0])
        elif index == 4:
            self.la_result_output.setText(percentage(float(first_value), float(second_value))[0])
        elif index == 5:
            if re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            self.la_result_output.setText(gross_of_net(float(first_value), float(second_value))[0])
        elif index == 6:
            if re.search('^-.*$', first_value):
                print("Don't use negative values")
                return
            self.la_result_output.setText(net_of_gross(float(first_value), float(second_value))[0])
        else:
            print("Please select a branch function first")
