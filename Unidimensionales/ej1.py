# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array(longitud:int, valor_inicial=0) -> list|None:
    return [valor_inicial] * longitud


print(crear_array(3, 5))
