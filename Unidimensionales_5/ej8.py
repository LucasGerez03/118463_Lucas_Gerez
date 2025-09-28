# Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# Una lista de nombres (lista_nombres).
# Un nombre a buscar en la lista (nombre_antiguo).
# Un nombre de reemplazo (nombre_nuevo).
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    contador = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i].lower() == nombre_antiguo.lower():
            lista_nombres[i] = nombre_nuevo
            contador += 1      
    return contador


nombres = ["Ana", "Luis", "Ana", "Carlos", "Ana", "Ana"]
reemplazos = reemplazar_nombres(nombres, "aNa", "lukitas")
print(nombres)
print(f"Cantidad de reemplazos realizados: {reemplazos}")
