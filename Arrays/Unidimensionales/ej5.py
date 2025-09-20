# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def producto_de_lista(lista_num=[]) -> float|None:
    if len(lista_num) == 0:   #si está vacia None
        return None
    producto = 1
    try:
        for numero in lista_num: 
            producto *= numero
        return producto
    except(TypeError):
        return None

print(producto_de_lista([]))
print(producto_de_lista(["asdd", 242, [2,4,2]]))
print(producto_de_lista([1,2,3,4,2]))

