def percent_of(fundamental_value: float | int, percentage: float | int):
    partial_value = fundamental_value * (percentage / 100)
    solution = f"{fundamental_value} x ({percentage} / 100))"
    return str(partial_value), solution


def percentage(fundamental_value: float | int, partial_value: float | int):
    percent = (partial_value / fundamental_value) * 100
    solution = f"({partial_value} / {fundamental_value}) x 100"
    return str(percent), solution


def gross_of_net(net: float | int, tax: float | int):
    gross = net / 100 * (100 + tax)
    solution = f"{net} / 100 * (100 + {tax})"
    return str(gross), solution


def net_of_gross(gross: float | int, tax: float | int):
    net = gross / (100 + tax) * 100
    solution = f"{gross} / (100 + {tax}) * 100"
    return str(net), solution


def subtract_percentage(fundamental_value: float | int, percentage: float | int):
    subtracted_percentage = fundamental_value - (fundamental_value * (percentage / 100))
    solution = f"{fundamental_value} - ({fundamental_value} x ({percentage} / 100))"
    return str(subtracted_percentage), solution


def add_percentage(fundamental_value: float | int, percentage: float | int):
    added_percentage = fundamental_value + (fundamental_value * (percentage / 100))
    solution = f"{fundamental_value} + ({fundamental_value} x ({percentage} / 100))"
    return str(added_percentage), solution
