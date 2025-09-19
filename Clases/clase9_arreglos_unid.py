

# Crear una lista con números del 1 al 5, agregar el 6, y luego eliminar el 2.
lista_num = [1, 2, 3, 4, 5]
lista_num.append(6)
lista_num.remove(3)
# print("Lista de números después de agregar 6 y eliminar 2:", lista_num)


# Crear una lista con nombres de tus amigos y ordenarla alfabéticamente.

lista_amigos = ["Lucas", "Ana", "Pedro", "María"]
lista_amigos.sort()




# Contar cuántas veces aparece el número 3 en una lista.
lista_numeros = [1, 2, 3, 4, 3, 5, 3]
contador_tres = lista_numeros.count(3)



# Invertir una lista de frutas.
lista_frutas = ["manzana", "banana", "cereza", "durazno"]
lista_frutas.reverse()
# print("Lista de frutas invertida:", lista_frutas)



# Hacer la suma de todos los números en una lista.
suma_numeros = sum(lista_numeros)


# Slicing
# print("Suma de todos los números en la lista:", suma_numeros)
# print("Cantidad de veces que aparece el número 3:", contador_tres)
# print("Lista de amigos ordenada alfabéticamente:", lista_amigos)
# print("Lista de frutas invertida:", lista_frutas)
# print("Lista de números después de agregar 6 y eliminar 2:", lista_num)


mi_lista = [1, 3, 5, 7, 9, 11, 13, 40, 39, 73, 115]
buscar = 40
#  1 -Búsqueda lineal (el más simple)
for i in list(range(len(mi_lista))):
    if mi_lista[i] == buscar:
        print(f"Encontrado {buscar} en el índice {i}")
        break

#  2 -Buscar el índice de un valor
indice = mi_lista.index(buscar)
print(f"El índice de {buscar} es: {indice}")



#  3 -Búsqueda binaria (requiere lista ordenada)


