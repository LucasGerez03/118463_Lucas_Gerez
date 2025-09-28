# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.

def diferencia_entre_arrays(array_1:list, array_2:list)-> list|None:
    diferencia = []
    for numero in array_1:
        if numero not in array_2 and numero not in diferencia:
            diferencia.append(numero)
    return diferencia
    
listorti_1= [1,2,3,4,5]
listorti_2= [3,4,5,6,7]
print(diferencia_entre_arrays(listorti_1, listorti_2))