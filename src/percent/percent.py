def percent_of(fundamental_value: float | int, percentage: float | int):
    partial_value = round(fundamental_value * (percentage / 100), 6)
    solution = f"{fundamental_value} x ({percentage} / 100))"
    return str(partial_value), solution


def percentage(fundamental_value: float | int, partial_value: float | int):
    percent = round((partial_value / fundamental_value) * 100, 6)
    solution = f"({partial_value} / {fundamental_value}) x 100"
    return str(percent), solution


def gross_of_net(net: float | int, tax: float | int):
    gross = round(net / 100 * (100 + tax), 2)
    solution = f"{net} / 100 * (100 + {tax})"
    return str(gross), solution


def net_of_gross(gross: float | int, tax: float | int):
    net = round(gross / (100 + tax) * 100, 2)
    solution = f"{gross} / (100 + {tax}) * 100"
    return str(net), solution


def subtract_percentage(fundamental_value: float | int, percentage: float | int):
    subtracted_percentage = round(fundamental_value - (fundamental_value * (percentage / 100)), 6)
    solution = f"{fundamental_value} - ({fundamental_value} x ({percentage} / 100))"
    return str(subtracted_percentage), solution


def add_percentage(fundamental_value: float | int, percentage: float | int):
    added_percentage = round(fundamental_value + (fundamental_value * (percentage / 100)), 6)
    solution = f"{fundamental_value} + ({fundamental_value} x ({percentage} / 100))"
    return str(added_percentage), solution
