# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
def union_entre_arrays(array_uno:list, array_dos:list) -> list|None :
    union = array_uno
    for numero in array_dos:
        if numero not in union:
            union.append(numero)
    return union  
# print(union_entre_arrays([1,2,3,4,5,6],[3,6,5,7,8,3,4,6,7,]))


def diferencia_entre_arrays(array_1:list, array_2:list)-> list|None:
    diferencia = []
    for numero in array_1:
        if numero not in array_2 and numero not in diferencia:
            diferencia.append(numero)
    return diferencia
    
listorti_1= [1,2,3,4,5]
listorti_2= [3,4,5,6,7]
print(diferencia_entre_arrays(listorti_1, listorti_2))