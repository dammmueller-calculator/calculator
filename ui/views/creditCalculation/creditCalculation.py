from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QTextEdit, QLabel, QMessageBox, QLineEdit, QDoubleSpinBox, QSpinBox
from PyQt6.QtCore import QObject, QEvent
from ui.views.InputModule import InputModule
from src.creditCalculation.creditCalc import calculate_credit


class CreditCalculation(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        # Lade UI-Datei
        uic.loadUi("ui/views/creditCalculation/creditCalculation.ui", self)

        # Referenzen zu UI-Elementen setzen
        self.tb_credit_amount = self.findChild(QLineEdit, "tb_credit_amount")
        self.dsb_interest_rate = self.findChild(QDoubleSpinBox, "dsb_interest_rate")
        self.tb_term = self.findChild(QSpinBox, "tb_term")
        self.la_monthly_rate = self.findChild(QLabel, "la_monthly_rate")
        self.la_total_cost = self.findChild(QLabel, "la_total_cost")
        self.la_total_interest = self.findChild(QLabel, "la_total_interest")

        # Event-Filter für Fokus-Handling setzen
        self.tb_credit_amount.installEventFilter(self)
        self.dsb_interest_rate.installEventFilter(self)
        self.tb_term.installEventFilter(self)

        # Suche Widget für Eingabe-Modul und setze Layout
        input_widget = self.findChild(QWidget, "wi_inputModule")
        layout = QVBoxLayout()
        input_widget.setLayout(layout)

        # Eingabe-Modul erstellen und ins Layout einfügen
        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        # Variable für das zuletzt fokussierte Eingabefeld
        self.last_focused_edit = None

        # Signale verbinden
        self.input_module.number_pressed.connect(self.update_input_line)
        self.input_module.sign_pressed.connect(self.handle_signal)

    def eventFilter(self, obj: QObject, event: QEvent):
        """ Event-Filter, um das zuletzt fokussierte Textfeld zu speichern """
        if event.type() == QEvent.Type.FocusIn:
            if obj in (self.tb_credit_amount, self.tb_interest_rate, self.tb_term):
                self.last_focused_edit = obj
        return super().eventFilter(obj, event)

    def update_input_line(self, value):
        """ Fügt eine gedrückte Zahl zum aktuell fokussierten Eingabefeld hinzu """
        if self.last_focused_edit:
            text = self.last_focused_edit.toPlainText()
            self.last_focused_edit.setPlainText(text + value)

    def handle_signal(self, value):
        """ Behandelt Sonderzeichen-Tasten (= für Berechnung, C für Reset) """
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
        """ Führt die Kreditberechnung durch und zeigt die Ergebnisse an """
        credit_amount = self.tb_credit_amount.toPlainText()
        interest_rate = self.tb_interest_rate.toPlainText()
        term = self.tb_term.toPlainText()

        # Überprüfung, ob alle Felder ausgefüllt sind
        if not credit_amount or not interest_rate or not term:
            QMessageBox.warning(self, "Fehlende Eingabe", "Bitte alle Werte eingeben.")
            return

        try:
            # Konvertiere Eingaben in numerische Werte
            credit_amount = float(credit_amount)
            interest_rate = float(interest_rate)
            term = int(term)
        except ValueError:
            QMessageBox.critical(self, "Fehlerhafte Eingabe", "Bitte gültige Zahlen eingeben.")
            return

        # Berechnung Kreditraten und Gesamtkosten
        monthly_rate, total_cost, total_interest = calculate_credit(credit_amount, interest_rate, term)

        # Ergebnisse in Labels anzeigen
        self.la_monthly_rate.setText(f"{monthly_rate:.2f} €")
        self.la_total_cost.setText(f"{total_cost:.2f} €")
        self.la_total_interest.setText(f"{total_interest:.2f} €")

        # Speichert Berechnung in History des Hauptfensters
        if self.parent:
            self.parent.appendHistory(f"Kreditberechnung: {credit_amount}€ | {interest_rate}% | {term} Monate")



