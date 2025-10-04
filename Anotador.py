##############################################################################
# clase 2


# CTRL + }

"CASTING"

"DONT REPEAT YOURSELF" "filosofia de desarrollo para poder evitar repetir codigo"

"PYTHON lenguaje de interpretado, para pasar instrucciones en codigo legible para las personas a codigo maquina"

"lenguajes COMPILADOS e INTERPRETADOS"

"python es multiplaformico, significa que puede correr en cualquier sistema operativo"

"agente de programacion, es"

##############################################################################
# clase 3

"""variables representativas y descriptivas

PEP8

"""

# Kanban , trelo


"""continue es para "saltear" lo q pasa, y seguir iterando
el brak es para literalmente parar todo """


"""AIzaSyCVa52LS3CG6jfA2IZwlG2-5uhDOkN_9iI"""

##############################################################################
#!Clase 4

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#? thislist 

#thisset CONJUNTO DE DATOS/ELEMENTOS QUE NO SE REPITEN Y ESTAN ORDENADOS, TAMBIEN MUTABLES

#pass

#SE PUEDE PONER else en While y Match

##############################################################################
#TODO Clase 5  CLASE FUNCIONES 
#!esta no #############################################
def sumo_dos_numeros(num1:int, num2:int) -> int:
    resultado = num1 + num2
    print(resultado)
    return 

#?esta si#############################################
def sumo_otros_numeros(num1:int, num2:int) -> int:
    resultado = num1 + num2 
    return resultado

# poner el return es por fomralidad, puede haber funciones que no retuornen nada


############################################################################

# clase 6 

#Los inputs por lo general se ponen afuera de las funciones

# Pasar por referencia una lista o diccionario, hace que se modifique el original (mutable) por su posicion de memoria
# Pasar por valor una variable simple (int, str, float) hace que no se modifique el original (immutable)


## clase 7
#SLICING
# PRINT(letara[comienzo:fin:paso])

#abs() solamente devuelve el numero en positivo si pasa un negativo
#abs(-5) devuelve 5
#abs(2.4) devuelve 2.4

list()

#################################################################################
# import sys
# import os
# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)

#################################################################################
ejemplo = "               hOLa Mundo                  "
# =========================CADENAS===========================
# FUNCIONES Y METODOS COMUNES DE STRINGS
# print(ejemplo.strip())   #→ elimina espacios al inicio y al final
# print(ejemplo.lstrip())  #→ elimina solo a la izquierda
# print(ejemplo.rstrip())  #→ elimina solo a la derecha
# print("===================")
# print(ejemplo.upper())    #-> Mayuscula
# print(ejemplo.lower())    #-> Minuscula
# print(ejemplo.capitalize())   #-> Primera letra en mayusucla #!si hay espacios no lo toma
# print(ejemplo.title())    #-> Cada palabra en mayuscula
print("===================")
print(ejemplo.find("Mundo"))   #→ posición donde empieza "Mundo"
print(ejemplo.count("o"))      #→ cuántas veces aparece la letra "o"
print("Hola" in ejemplo)       # True → verifica si existe
print("Python" not in ejemplo) # True → verifica si no existe
print("===================")
print(ejemplo.replace("Mundo", "Python"))  # "  Hola Python  "
print("===================")


frase = "manzana,pera,banana"
lista = frase.split(",") 
print(lista)
print("===================")
print("-h-".join(lista))


##################################################################################################
# =============================
# Algoritmos de Ordenamiento #!SELECTION_SORT
# =============================
#
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# =============================
# Algoritmos de Ordenamiento #!BUBBLE_SORT
# =============================

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# =============================
# Algoritmos de Ordenamiento #!QUICK_SORT
# =============================

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# =============================
# Algoritmos de Ordenamiento #!MERGE_SORT
# =============================

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# =============================
# Algoritmos de Ordenamiento #!INSERTION_SORT
# =============================

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#######################################################
# import sys
# import os

# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)

#######################################################