# Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de ser True ordena el vector en forma descendente.
# Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, y devuelva un único vector también ordenado. La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.
# Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
# Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.


import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from libreria.funciones import * 

es_par_o_impar(5)
