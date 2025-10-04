def esta_entre(num, num1, num2): #validacion del ingreso del numero en rango
    if num >= num1 and num <= num2:
        return True
    else:
        return False
    
def es_positivo(num) -> bool | None:
        try:
            if num >= 0:
                return True
            else:
                return False
        except (TypeError):
            return None
        
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False