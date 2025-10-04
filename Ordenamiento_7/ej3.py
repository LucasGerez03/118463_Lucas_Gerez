# Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 

# Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from libreria.funciones import es_positivo


def ordenar_positivos_y_negativos(vector=[]) :
        negativos = []
        positivos = []
        for num in vector:
            if es_positivo(num):
                positivos.append(num)
            else:
                negativos.append(num)         
        negativos.sort(reverse=True)
        positivos.sort()
        lista = negativos + positivos
        return f"La lista esperada es: {lista}\n(Negativos/Decreciente): {negativos}\n(Positivos/Creciente): {positivos}" 

    


