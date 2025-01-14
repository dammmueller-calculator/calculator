from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication

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
        if self.combox_branch_function_select.currentIndex() != 0:
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

    def handle_input_on_function_select(self):
        index = self.combox_function_select.currentIndex()

        if index == 1:
            self.la_first_input.setText("Fakultät")
            self.tb_first_input.setVisible(True)
        elif index == 2:

        elif index == 3:

        elif index == 4:

        elif index == 5:

        else:
            self.la_first_input.setText("")
            self.la_second_input.setText("")
            self.tb_first_input.setVisible(False)
            self.tb_second_input.setVisible(False)

    def handle_result_on_signal(self):
        result = ''
        index = self.combox_function_select.currentIndex()

        if index == 1:

        elif index == 2:

        elif index == 3:

        elif index == 4:

        elif index == 5:

        else:
            print("Please select a branch function first")
            return

        if result != '':
            self.la_result_output.setText(result[0])
            self.parent.appendHistory(result[1])
        else:
            return
