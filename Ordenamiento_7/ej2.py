# Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, y devuelva un único vector también ordenado. La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.

import ej1 as ord


def intercalar_vectores_1(vector_1:list, vector_2:list, descendente=False) -> list|None : 
    lista = vector_1 + vector_2
    if descendente:
        lista = ord.ordenar_array(lista, True)
    else:
        lista = ord.ordenar_array(lista)

    return lista

print(intercalar_vectores_1([5,6,7,8], [1,2,3,4]))
print(intercalar_vectores_1([5,6,7,8], [1,2,3,4], True))
