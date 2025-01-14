from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtCore import pyqtSignal
from ui.views.InputModule import InputModule

class CalculatorModule(QWidget):
    def __init__(self):
        super().__init__()
        
        # Layout für den Taschenrechner
        layout = QVBoxLayout(self)
        
        # Eingabefeld
        self.input_line = QLineEdit(self)
        self.input_line.setReadOnly(True)  # Das Eingabefeld ist schreibgeschützt
        self.input_line.setText("0")  # Standardwert
        
        # InputModule hinzufügen
        self.input_module = InputModule()
        
        # Layout zusammenfügen
        layout.addWidget(self.input_line)
        layout.addWidget(self.input_module)
        self.setLayout(layout)

        # Signale verbinden
        self.input_module.number_pressed.connect(self.append_to_expression)
        self.input_module.sign_pressed.connect(self.process_sign)

        # Interne Variable für den aktuellen Ausdruck
        self.current_expression = ""

    def append_to_expression(self, value):
        """Fügt Zahlen oder Punkt/Komma zur Eingabe hinzu."""
        if self.current_expression == "0":  # Anfangszeichen "0" ersetzen
            self.current_expression = ""
        self.current_expression += value
        self.update_display()

    def process_sign(self, sign):
        """Bearbeitet Rechenoperationen oder spezielle Zeichen."""
        if sign == "=":
            self.calculate_result()
        elif sign == "C":
            self.clear_expression()
        else:
            self.current_expression += f" {sign} "
            self.update_display()

    def calculate_result(self):
        """Berechnet das Ergebnis des aktuellen Ausdrucks."""
        try:
            # Ersetze Komma durch Punkt für Dezimalzahlen
            expression = self.current_expression.replace(",", ".")
            result = eval(expression)  # Vorsicht bei eval, besser nur für kontrollierte Ausdrücke
            self.current_expression = str(result).replace(".", ",")  # Rückumwandlung für Anzeige
            self.update_display()
        except Exception:
            self.current_expression = "Error"
            self.update_display()

    def clear_expression(self):
        """Setzt den aktuellen Ausdruck zurück."""
        self.current_expression = "0"
        self.update_display()

    def update_display(self):
        """Aktualisiert das Eingabefeld."""
        self.input_line.setText(self.current_expression)
