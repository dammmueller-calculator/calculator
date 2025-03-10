def calculate_credit(credit_amount: float | int, interest_rate: float | int, term: int | float):
    # Berechnung monatliche Zinsrate
    # Zinssatz wird durch 100 und durch 12 geteilt um monatlichen Zinssatz zu berechnen
    rate = interest_rate / 100 / 12
    # Laufzeit Kredit in Monaten
    months = term

    # Berechnung monatliche Rate mit Formel für Annuitätsdarlehen
    # Annuitätsdarlehen: monatliche Rate = Kreditbetrag * Zinssatz / (1 -(1 + Zinssatz) ^ -Laufzeit)
    # Berechnung konstanter monatlicher Rate für  gesamte Laufzeit
    monthly_rate = (credit_amount * rate) / (1 - (1 + rate) ** -months)

    # Berechnung gesamte Zinsen
    # Gesamtzinsen = Gesamtkosten - Kreditbetrag (Kreditbetrag muss von gesamter Zahlungen abgezogen werden)
    total_cost = monthly_rate * months
    total_interest = total_cost - credit_amount
    # Lösung als String
    solution = f"Monatliche Rate = ({credit_amount} * {rate}) / (1 - (1 + {rate}) ^ -{months})"

    # Rückgabe berechnete Werte als String (monatliche Rate, Gesamtkosten, Zinsen)
    return str(monthly_rate), str(total_cost), str(total_interest), solution

