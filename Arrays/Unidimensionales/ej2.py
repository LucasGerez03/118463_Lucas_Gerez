# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
from ej1 import crear_array

def ingresar_numeros(cantidad:int) -> list|None:
        array = crear_array(cantidad)
        for i in range(cantidad):
            numero = int(input(f"Ingrese el número {i+1}: "))
            array[i] = numero
        return array

# print(ingresar_numeros(3)) 