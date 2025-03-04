def calculate_credit(credit_amount: float, interest_rate: float, term: int):

    # berechnung monatlicher zinssatz
    monthly_interest_rate = (interest_rate / 100) / 12

    # berechnung monatlicher rate
    if monthly_interest_rate != 0:
        monthly_rate = credit_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** term) / \
                       ((1 + monthly_interest_rate) ** term - 1)
    else:
        monthly_rate = credit_amount / term  # falls zinssatz 0%

    # berechnung gesamtkosten kredit
    total_cost = monthly_rate * term

    # berechnung gesamtzinsen
    total_interest = total_cost - credit_amount

    return monthly_rate, total_cost, total_interest
