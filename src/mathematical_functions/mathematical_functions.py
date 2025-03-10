def calculate_faculty(faculty: int):
    history = f"{faculty}! = {faculty}"
    i = 0
    counter = faculty - 1
    result = faculty

    while i < faculty - 1:
        history += f" * {counter}"
        result = result * counter
        counter = counter - 1
        i = i + 1

    return f"{faculty}! = {result}", history


def calculate_square_root(radical: int):
    square_root = radical ** .5
    return str(square_root), f"Square root of {radical}: {square_root}"


def power_function(func: str):
    power = int(func.split("^")[1])
    base = int(func.split("^")[0])
    result = base
    result_str = f"{func} = {base} "

    for i in range(power - 1):
        result = result * base
        result_str += f"* {base}"

    return str(result), f"{result_str} = {result}"


def find_prime_numbers(lower_limit: int, upper_limit: int):
    i = lower_limit
    number = lower_limit + 1
    result = ""

    while i < upper_limit:
        if not (
            number != 2 and (number % 2) == 0 or
            number != 3 and (number % 3) == 0 or
            number != 5 and (number % 5) == 0 or
            number != 7 and (number % 7) == 0
        ):
            if result == "":
                result = f"{number}"
            else:
                result += f", {number}"
        i = i + 1
        number = number + 1

    return result, f"Primzahlen zwischen {lower_limit} und {upper_limit}: {result}"


def convert_fraction(fraction: str):
    split_string = fraction.split("/")
    result = int(split_string[0]) / int(split_string[1])
    return str(result), f"{fraction} = {result}"
