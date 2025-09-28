#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

def union_entre_arrays(array_uno:list, array_dos:list) -> list|None :
    union = array_uno
    for numero in array_dos:
        if numero not in union:
            union.append(numero)
    return union  
print(union_entre_arrays([1,2,3,4,5,6],[3,6,5,7,8,3,4,6,7,]))
