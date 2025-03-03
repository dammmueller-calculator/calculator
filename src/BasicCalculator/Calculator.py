def add(x, y):
    return x + y

def checksign(sign):
    # Klammer
    # Case 1: sign = "("    
    if sign == "*":
        return "*"
    elif sign == "÷":
        return "/"
    elif sign == "−":
        return "-"
    elif sign == "+":
        return "+"
    elif sign == "=":
        return "="
    else:
        return sign


       
