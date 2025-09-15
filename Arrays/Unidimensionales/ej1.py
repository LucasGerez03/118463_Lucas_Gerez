# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array(longitud:int, valor_inicial=0) -> list|None:
    try:
        array = [valor_inicial] * longitud
        return array    
    except TypeError:
        return None


print(crear_array(1))
