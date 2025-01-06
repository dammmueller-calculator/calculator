from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class Percent(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/views/percent/percent.ui", self)

    def handleLabelsOnSelectChange(self):
        index = self.combox_branchFunctionSelect.currentIndex()
        if (index == 1) or (index == 2) or (index == 3):
            self.la_firstInput.setText("Grundwert")
            self.la_secondInput.setText("Prozentsatz")
        elif index == 4:
            self.la_firstInput.setText("Grundwert")
            self.la_secondInput.setText("Prozentwert")
        elif index == 5:
            self.la_firstInput.setText("Nettopreis")
            self.la_secondInput.setText("Steuersatz")
        elif index == 6:
            self.la_firstInput.setText("Bruttopreis")
            self.la_secondInput.setText("Steuersatz")
        else:
            self.la_firstInput.setText("")
            self.la_secondInput.setText("")
