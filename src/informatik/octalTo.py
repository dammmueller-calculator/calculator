from .decimalTo import decimal_to_binary, decimal_to_ternary, decimal_to_hex

def octal_to_decimal(text) -> str:
    try:
        # Konvertiere String-Eingabe in Integer
        decimal = int(text, 8)
        
        return str(decimal)
        
    except ValueError:
        return "Fehler: Ungültige Oktalzahl"
    
def octal_to_binary(text) -> str:
    try:
        # Nutze octal_to_decimal() und decimal_to_binary()
        decimal = int(text, 8)
        binary = decimal_to_binary(str(decimal))
        
        return binary
        
    except ValueError:
        return "Fehler: Ungültige Oktalzahl"
def octal_to_ternary(text) -> str:
    try:
        # Nutze octal_to_decimal() und decimal_to_ternary()
        decimal = int(text, 8)
        ternary = decimal_to_ternary(str(decimal))
        
        return ternary
        
    except ValueError:
        return "Fehler: Ungültige Oktalzahl"

def octal_to_hex(text) -> str:
    try:
        # Nutze octal_to_decimal() und decimal_to_hex()
        decimal = int(text, 8)
        hex_result = decimal_to_hex(str(decimal))
        
        return hex_result
        
    except ValueError:
        return "Fehler: Ungültige Oktalzahl"            