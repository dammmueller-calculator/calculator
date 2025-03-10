from .decimalTo import decimal_to_binary, decimal_to_ternary, decimal_to_octal

def hex_to_decimal(text) -> str:
    try:
        # Nutze Python's eingebaute int() Funktion:
        # 1. int() konvertiert Hex-String in Dezimalzahl
        # 2. .upper() konvertiert zu Großbuchstaben
        decimal = int(text, 16)
        
        return str(decimal)
        
    except ValueError:
        return "Fehler: Ungültige Hexadezimalzahl" 

def hex_to_binary(text) -> str:
    try:
        # Nutze hex_to_decimal() und decimal_to_binary()
        decimal = int(text, 16)
        binary = decimal_to_binary(str(decimal))
        
        return binary
        
    except ValueError:
        return "Fehler: Ungültige Hexadezimalzahl" 

def hex_to_ternary(text) -> str:
    try:
        # Nutze hex_to_decimal() und decimal_to_ternary()
        decimal = int(text, 16)
        ternary = decimal_to_ternary(str(decimal))
        
        return ternary
        
    except ValueError:
        return "Fehler: Ungültige Hexadezimalzahl"

def hex_to_octal(text) -> str:
    try:
        # Nutze hex_to_decimal() und decimal_to_octal()
        decimal = int(text, 16)
        octal = decimal_to_octal(str(decimal))
        
        return octal
        
    except ValueError:
        return "Fehler: Ungültige Hexadezimalzahl"           