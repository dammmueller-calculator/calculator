from .decimalTo import decimal_to_binary, decimal_to_hex, decimal_to_octal

def ternary_to_decimal(text) -> str:
    try:
        # Konvertiere String-Eingabe in Integer
        decimal = int(text)
        
        # Spezialfall: Wenn Eingabe 0 ist
        if decimal == 0:
            return "0"
        
        # Liste für ternäre Ziffern (wird von links aufgebaut)
        ternary_digits = []
        temp = decimal
        
        # Divisions-Algorithmus:
        # 1. Teile Zahl durch 3
        # 2. Rest (0, 1 oder 2) ist ternäre Ziffer
        # 3. Ganzzahl-Ergebnis wird neue Zahl
        # 4. Wiederholen bis Zahl = 0
        while temp > 0:
            remainder = temp % 3      # Rest der Division (0, 1 oder 2)
            ternary_digits.insert(0, str(remainder))  # Füge Rest vorne ein
            temp //= 3               # Ganzzahldivision durch 3
        
        # Verbinde alle Ziffern zu einem String
        return "".join(ternary_digits)
            
    except ValueError:
        return "Fehler: Ungültige Dezimalzahl"
    
def ternary_to_binary(text) -> str:
    try:
        # Nutze ternary_to_decimal() und decimal_to_binary()
        decimal = int(text, 3)
        binary = decimal_to_binary(str(decimal))
        
        return binary
        
    except ValueError:
        return "Fehler: Ungültige Ternäre Zahl"

def ternary_to_hex(text) -> str:
    try:
        # Nutze ternary_to_decimal() und decimal_to_hex()
        decimal = int(text, 3)
        hex_result = decimal_to_hex(str(decimal))
        
        return hex_result
        
    except ValueError:
        return "Fehler: Ungültige Ternäre Zahl"

def ternary_to_octal(text) -> str:
    try:
        # Nutze ternary_to_decimal() und decimal_to_octal()
        decimal = int(text, 3)
        octal = decimal_to_octal(str(decimal))
        
        return octal
        
    except ValueError:
        return "Fehler: Ungültige Ternäre Zahl"            