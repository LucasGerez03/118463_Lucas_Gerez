# Realizar los siguientes módulos:
# Validate.py
# validate_number()
# validate_length()

# Nota: estas funciones las tendrán que desarrollar en el módulo Validate y utilizar en el módulo Input.py para realizar las validaciones necesarias.

def validate_number(numero: float, max: float, min: float) -> bool|None:
    if numero >= min and numero <= max:
        return True
    else:
        print("ERROR: Número ingresado Inválido")
        return False

def validate_length(longitud: int, cadena: str) -> bool|None:
    if len(cadena) == longitud:
        return True
    else:
        print("ERROR: Cadena ingresada Inválida")
        return False
    
    
        