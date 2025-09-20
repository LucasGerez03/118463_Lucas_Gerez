# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

###Punto 1###
def crear_array(longitud:int, valor_inicial=0) -> list|None:
    return [valor_inicial] * longitud

def ingresar_numeros(cantidad:int) -> list|None:
        array = crear_array(cantidad)
        for i in range(cantidad):
            numero = int(input(f"Ingrese el número {i+1}: "))
            array[i] = numero
        return array

print(ingresar_numeros(7)) 