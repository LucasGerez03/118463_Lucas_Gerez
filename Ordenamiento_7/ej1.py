# Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de ser True ordena el vector en forma descendente.
# Crear una función que reciba como parámetro un vector de números enteros. La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
# Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.


def ordenar_array(array, descendente=False):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if descendente:
                # Orden descendente: si el elemento actual es MENOR que el siguiente, se intercambian
                if array[j] < array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
            else:
                # Orden ascendente (por defecto): si el elemento actual es MAYOR que el siguiente, se intercambian
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp

        # Si no hubo ningún intercambio en el bucle interno, el array está ordenado
    return array

# lista_num = [5, 1, 4, 2, 8, 3]
# print(f"Array original: {lista_num}")
# print(f"Array ascendente: {ordenar_array(lista_num)}")
# # 