from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from ui.views.InputModul import InputModul
from src.percent.percent import PercentLib


class Percent(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/percent/percent.ui", self)
        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)
        self.input_module = InputModul()
        layout.addWidget(self.inputModule)
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
        first_value = self.tb_first_input.text()
        second_value = self.tb_second_input.text()
        if index == 1:
            PercentLib.add_percentage(PercentLib(), first_value, second_value)
        elif index == 2:
            print("")
        elif index == 3:
            print("")
        elif index == 4:
            print("")
        elif index == 5:
            print("")
        elif index == 6:
            print("")
        else:
            print("Please select a branch function first")
