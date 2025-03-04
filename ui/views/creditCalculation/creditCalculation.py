from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from ui.views.InputModule import InputModule
from src.creditCalculation.creditCalc import *


class CreditCalculation(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        # lade ui-file für kreditrechner
        uic.loadUi("ui/views/creditCalculation/creditCalculation.ui", self)

        # suche widget für eingabe-modul und setze layout
        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        # erstelle instanz eingabe-modul und füge es layout hinzu
        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        # variable zum speichern des zuletzt fokussierten eingabefelds
        self.last_focused_edit = None

        # verbinden signale eingabe-modul mit entsprechenden methoden
        self.input_module.number_pressed.connect(self.update_input_line)
        self.input_module.sign_pressed.connect(self.handle_signal)

    def find_last_selected_text_edit(self):
        # ermittelt zuletzt fokussiertes eingabefeld und speichert es
        if QApplication.focusWidget() == self.tb_credit_amount:
            self.last_focused_edit = self.tb_credit_amount
        if QApplication.focusWidget() == self.tb_interest_rate:
            self.last_focused_edit = self.tb_interest_rate
        if QApplication.focusWidget() == self.tb_term:
            self.last_focused_edit = self.tb_term

    def update_input_line(self, value):
        # aktualisiert das aktuell fokussierte eingabefeld mit gedrückter zahl
        text = self.last_focused_edit.toPlainText()
        self.last_focused_edit.setPlainText(text + value)

    def handle_signal(self, value):
        # verarbeitet das drücken von sondertasten (= für berechnung / C für zurücksetzen)
        if value == "=":
            self.calculate_credit()
        elif value == "C":
            self.tb_credit_amount.setPlainText("")
            self.tb_interest_rate.setPlainText("")
            self.tb_term.setPlainText("")
            self.la_monthly_rate.setText("")
            self.la_total_cost.setText("")
            self.la_total_interest.setText("")

    def calculate_credit(self):
        # führt kreditberechnung durch und zeigt ergebnisse an
        credit_amount = self.tb_credit_amount.toPlainText()
        interest_rate = self.tb_interest_rate.toPlainText()
        term = self.tb_term.toPlainText()

        # überprüfung ob alle felder ausgefüllt sind
        if not credit_amount or not interest_rate or not term:
            print("Bitte alle Werte eingeben.")
            return

        try:
            # konvertiere eingaben in die richtigen datentypen
            credit_amount = float(credit_amount)
            interest_rate = float(interest_rate)
            term = int(term)
        except ValueError:
            print("Ungültige Eingabe.")
            return

        # berechnung der kreditraten und gesamtkosten
        monthly_rate, total_cost, total_interest = calculate_credit(credit_amount, interest_rate, term)

        # ergebnisse in den entsprechenden labels anzeigen
        self.la_monthly_rate.setText(f"{monthly_rate:.2f} €")
        self.la_total_cost.setText(f"{total_cost:.2f} €")
        self.la_total_interest.setText(f"{total_interest:.2f} €")

        # speichert berechnung in history des hauptfensters
        self.parent.appendHistory(f"Kreditberechnung: {credit_amount}€ | {interest_rate}% | {term} Monate")

