from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from ui.views.InputModule import InputModule
from src.creditCalc.creditCalc import *


class CreditCalculation(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        # Lade UI-File für Kreditrechner
        uic.loadUi("ui/views/creditCalculation/creditCalculation.ui", self)

        # Suche Widget für Eingabe-Modul und setz Layout
        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        # Erstelle Instanz Eingabe-Modul und füge es Layout hinzu
        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        # Variable zum Speichern des zuletzt fokussierten Eingabefelds
        self.last_focused_edit = None

        # Verbinden Signale Eingabe-Modul mit entsprechenden Methoden
        self.input_module.number_pressed.connect(self.update_input_line)
        self.input_module.sign_pressed.connect(self.handle_signal)

    def find_last_selected_text_edit(self):
        # Ermittelt zuletzt fokussiertes Eingabefeld und speichert es
        if QApplication.focusWidget() == self.tb_credit_amount:
            self.last_focused_edit = self.tb_credit_amount
        if QApplication.focusWidget() == self.tb_interest_rate:
            self.last_focused_edit = self.tb_interest_rate
        if QApplication.focusWidget() == self.tb_term:
            self.last_focused_edit = self.tb_term

    def update_input_line(self, value):
        # Aktualisiert das aktuell fokussierte Eingabefeld mit gedrückter Zahl
        text = self.last_focused_edit.toPlainText()
        self.last_focused_edit.setPlainText(text + value)

    def handle_signal(self, value):
        # Verarbeitet das Drücken von Sondertasten (= für Berechnung / C für Zurücksetzen)
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
        # Führt Kreditberechnung durch und zeigt Ergebnisse an
        credit_amount = self.tb_credit_amount.toPlainText()
        interest_rate = self.tb_interest_rate.toPlainText()
        term = self.tb_term.toPlainText()

        # Überprüfung ob alle Felder ausgefüllt sind
        if not credit_amount or not interest_rate or not term:
            print("Bitte alle Werte eingeben.")
            return

        try:
            # Konvertiere Eingaben in die richtigen Datentypen
            credit_amount = float(credit_amount)
            interest_rate = float(interest_rate)
            term = int(term)
        except ValueError:
            print("Ungültige Eingabe.")
            return

        # Berechnung der Kreditraten und Gesamtkosten
        monthly_rate, total_cost, total_interest = calculate_credit(credit_amount, interest_rate, term)

        # Ergebnisse in den entsprechenden Labels anzeigen
        self.la_monthly_rate.setText(f"{monthly_rate:.2f} €")
        self.la_total_cost.setText(f"{total_cost:.2f} €")
        self.la_total_interest.setText(f"{total_interest:.2f} €")

        # Speichert Berechnung in History des Hauptfensters
        self.parent.appendHistory(f"Kreditberechnung: {credit_amount}€ | {interest_rate}% | {term} Monate")
