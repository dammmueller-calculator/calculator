from .decimalTo import decimal_to_hex, decimal_to_ternary, decimal_to_octal

def binary_to_hex(text) -> str:
    try:
        # Nutze binary_to_decimal() und decimal_to_hex()
        decimal = int(text, 2)
        hex_result = decimal_to_hex(str(decimal))
        
        return hex_result
        
    except ValueError:
        return "Fehler: Ungültige Binärzahl"

def binary_to_decimal(text) -> str:
    try:
        # Nutze Python's eingebaute int() Funktion:
        # 1. int() konvertiert Binär-String in Dezimalzahl
        decimal = int(text, 2)
        
        return str(decimal)
        
    except ValueError:
        return "Fehler: Ungültige Binärzahl"    

def binary_to_ternary(text) -> str:
    try:
        # Nutze binary_to_decimal() und decimal_to_ternary()
        decimal = int(text, 2)
        ternary = decimal_to_ternary(str(decimal))
        
        return ternary
        
    except ValueError:
        return "Fehler: Ungültige Binärzahl"

def binary_to_octal(text) -> str:
    try:
        # Nutze binary_to_decimal() und decimal_to_octal()
        decimal = int(text, 2)
        octal = decimal_to_octal(str(decimal))
        
        return octal
        
    except ValueError:
        return "Fehler: Ungültige Binärzahl"        