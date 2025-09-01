from input import get_int

# Realizar una función recursiva que calcule la suma de los primeros números naturales:
def suma_numeros_naturales(numero: int) -> int:
    if numero == 1:  # caso base
        resultado = 1
    elif numero > 1:
        resultado = numero + suma_numeros_naturales(numero - 1)
    return resultado


print(suma_numeros_naturales(4))  # debería dar 10

