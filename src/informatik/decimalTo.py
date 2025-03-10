def decimal_to_binary(text) -> str:
    try:
        # Konvertiere String-Eingabe in Integer
        decimal = int(text)
        
        # Spezialfall: Wenn Eingabe 0 ist
        if decimal == 0:
            return "0"
        
        # Liste für binäre Ziffern (wird von links aufgebaut)
        binary_digits = []
        temp = decimal
        
        # Divisions-Algorithmus:
        # 1. Teile Zahl durch 2
        # 2. Rest (0 oder 1) ist binäre Ziffer
        # 3. Ganzzahl-Ergebnis wird neue Zahl
        # 4. Wiederholen bis Zahl = 0
        while temp > 0:
            remainder = temp % 2      # Rest der Division (0 oder 1)
            binary_digits.insert(0, str(remainder))  # Füge Rest vorne ein
            temp //= 2               # Ganzzahldivision durch 2
        
        # Verbinde alle Ziffern zu einem String
        return "".join(binary_digits)
            
    except ValueError:
        return "Fehler: Ungültige Dezimalzahl" 
        
def decimal_to_hex(text) -> str:   
    try:
        # Konvertiere String-Eingabe in Integer
        decimal = int(text)
        
        # Spezialfall: Wenn Eingabe 0 ist
        if decimal == 0:
            return "0"
            
        # Nutze Python's eingebaute hex() Funktion:
        # 1. hex() gibt String im Format "0x2A" zurück
        # 2. [2:] entfernt "0x" Prefix
        # 3. .upper() konvertiert zu Großbuchstaben
        hex_result = hex(decimal)[2:].upper()
        
        return hex_result
        
    except ValueError:
        return "Fehler: Ungültige Dezimalzahl"  

def decimal_to_ternary(text) -> str:
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

def decimal_to_octal(text) -> str:
    try:
        # Konvertiere String-Eingabe in Integer
        decimal = int(text)
        
        # Spezialfall: Wenn Eingabe 0 ist
        if decimal == 0:
            return "0"
        
        # Liste für oktale Ziffern (wird von links aufgebaut)
        octal_digits = []
        temp = decimal
        
        # Divisions-Algorithmus:
        # 1. Teile Zahl durch 8
        # 2. Rest (0 bis 7) ist oktale Ziffer
        # 3. Ganzzahl-Ergebnis wird neue Zahl
        # 4. Wiederholen bis Zahl = 0
        while temp > 0:
            remainder = temp % 8      # Rest der Division (0 bis 7)
            octal_digits.insert(0, str(remainder))  # Füge Rest vorne ein
            temp //= 8               # Ganzzahldivision durch 8
        
        # Verbinde alle Ziffern zu einem String
        return "".join(octal_digits)
            
    except ValueError:
        return "Fehler: Ungültige Dezimalzahl"      