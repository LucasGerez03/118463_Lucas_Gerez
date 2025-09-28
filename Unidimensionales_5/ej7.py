#Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def mostrar_posiciones_valor_maximo(lista: list) -> None:
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    maximo = max(lista)
    for i in range(len(lista)):
        if lista[i] == maximo:
            print(f"valor maximo: {maximo} , posicion {i}")  
# Ejemplo de uso
lista_enteros = [3, 5, 2, 9, 1, 9, 4]
mostrar_posiciones_valor_maximo(lista_enteros)


