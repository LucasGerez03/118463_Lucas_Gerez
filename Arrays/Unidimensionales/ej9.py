# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

def interseccion_de_arrays(array_uno:list, array_dos: list) -> list|None:
    interseccion = []
    for num_lista_uno in array_uno:     #bucle primera lista
        for num_lista_dos in array_dos:     #compara todos los elementos de la segunda lista
            if num_lista_uno == num_lista_dos and num_lista_dos not in interseccion:
                interseccion.append(num_lista_dos)
    interseccion.sort() #ordeno la lista en orden ascendente
    return interseccion

listorti_1= [1,2,4,3,5,6]
listorti_2= [4,6,5,7,8,3,4,6,7,]
print(interseccion_de_arrays(listorti_1, listorti_2))

