# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def posicion_del_numero_maximo(lista_num=[]) -> int|None:
    if  len(lista_num) == 0 or type(lista_num) != list: #si no es una lista o si está vacia
        return None
    maximo = max(lista_num)   
    return lista_num.index(maximo)

# print(posicion_del_numero([4,2,5,6,123,5,3]))
# print(posicion_del_numero(False))
# print(posicion_del_numero(355))
# print(posicion_del_numero(["asdasd"]))
# print(posicion_del_numero("sss"))