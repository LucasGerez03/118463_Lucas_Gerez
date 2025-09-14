# Realizar los siguientes módulos:
# Input.py
# get_int()
# get_float()
# get_string()
from validate import *

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    num = int(input(mensaje)) 
    while validate_number(num, maximo, minimo) == False: 
        reintentos -= 1
        if reintentos < 0:   
            return None     #fin de reintentos 
        print(mensaje_error)
        num = int(input(mensaje))
    return num  #fin del bucle

print(get_int("Ingrese un número entre 1 y 10: ", "Error, fuera de rango.", 1, 10, 1))