# 📌 Desafío: Verificación de un Cuadrado Mágico
# Un cuadrado mágico es una matriz cuadrada de n × n en la que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma. Esta suma se conoce como constante mágica (M), y se calcula con la siguiente fórmula:


# Formalmente, un cuadrado mágico de orden n contiene los números enteros del 1 al n², organizados de manera que cumplen la condición de igualdad en las sumas.
# 🔹 Objetivo
# Desarrollar un programa en Python que permita ingresar una matriz cuadrada de orden n y determine si es un cuadrado mágico.
# 🔹 Requisitos del Programa
# ✔️ Ingreso de datos:
# Permitir que el usuario ingrese la matriz manualmente o, de manera opcional, generar una aleatoria.
# Validar que los valores ingresados sean números enteros en el rango de 1 a n² y que no se repitan.
# Asegurar que la matriz ingresada tenga un tamaño válido (n × n).


# ✔️ Verificación del cuadrado mágico:
# Calcular la constante mágica según la fórmula.
# Comparar la suma de:
# Cada fila
# Cada columna
# Las dos diagonales principales
# Determinar si todas las sumas son iguales a la constante mágica.
# ✔️ Salida de resultados:
# Mostrar la matriz ingresada de forma clara y organizada.
# Indicar si la matriz es un cuadrado mágico o no.




# 📌 Extras opcionales:
#  ✅ Permitir que el usuario ingrese matrices de distintos tamaños (por ejemplo, 3×3, 4×4, etc.).
#  ✅ Mostrar mensajes de error en caso de ingreso inválido.
#  ✅ Implementar una opción para generar un cuadrado mágico válido automáticamente.

import random

def print_matrix(matrix):
    print("Matriz ingresada:")
    n = len(matrix)
    for row in matrix:
        print("  ".join(f"{num:2}" for num in row))
    print()

def input_matrix(n):
    print(f"Ingrese los {n*n} números (del 1 al {n*n}) separados por espacios o enter, fila por fila:")
    numbers = []
    while True:
        try:
            numbers = []
            while len(numbers) < n * n:
                entrada = input(f"Números restantes {n*n - len(numbers)}: ")
                nums = entrada.strip().split()
                if not all(num.isdigit() for num in nums):
                    print("Todos los valores deben ser números enteros.")
                    continue
                nums = list(map(int, nums))
                numbers.extend(nums)
            if len(numbers) != n * n:
                print(f"Debe ingresar exactamente {n*n} números.")
                continue
            if sorted(numbers) != list(range(1, n*n+1)):
                print(f"Los números deben ser únicos y estar en el rango de 1 a {n*n}.")
                continue
            # Construir la matriz
            matrix = [numbers[i*n:(i+1)*n] for i in range(n)]
            return matrix
        except Exception as e:
            print(f"Error en el ingreso: {e}. Intente nuevamente.")

def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = n * (n*n + 1) // 2

    # Suma de filas
    for row in matrix:
        if sum(row) != magic_sum:
            return False, magic_sum

    # Suma de columnas
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False, magic_sum

    # Diagonal principal
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False, magic_sum

    # Diagonal secundaria
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_sum:
        return False, magic_sum

    return True, magic_sum

def generate_magic_square(n):
    # Solo funciona para n impar (método de Siam)
    if n < 3:
        raise ValueError("No existe cuadrado mágico de orden menor a 3.")
    if n % 2 == 1:
        magic_square = [[0]*n for _ in range(n)]
        num = 1
        i, j = 0, n // 2
        while num <= n*n:
            magic_square[i][j] = num
            num += 1
            newi, newj = (i-1) % n, (j+1) % n
            if magic_square[newi][newj]:
                i += 1
            else:
                i, j = newi, newj
        return magic_square
    else:
        # Para n par, solo implementaremos el método para pares múltiplos de 4 (cuadrado mágico de orden par-par)
        if n % 4 == 0:
            magic_square = [[(n*y)+x+1 for x in range(n)] for y in range(n)]
            for i in range(n):
                for j in range(n):
                    if (i%4 == j%4) or ((i+j)%4 == 3):
                        magic_square[i][j] = n*n + 1 - magic_square[i][j]
            return magic_square
        else:
            # Orden par-impar (como 6x6, 10x10) requiere un método más complejo
            raise NotImplementedError("Solo se pueden generar automáticamente cuadrados mágicos de orden impar o múltiplos de 4.")

def main():
    print("=== Verificación de Cuadrado Mágico ===")
    while True:
        try:
            opcion = input("¿Desea ingresar manualmente la matriz (M), generar aleatoria válida (A) o salir (S)? [M/A/S]: ").strip().upper()
            if opcion == 'S':
                print("¡Hasta luego!")
                break

            n = int(input("Ingrese el tamaño de la matriz (n >= 3): "))
            if n < 3:
                print("El tamaño debe ser al menos 3.")
                continue

            if opcion == 'A':
                try:
                    matrix = generate_magic_square(n)
                    print("Se generó automáticamente un cuadrado mágico válido:")
                    print_matrix(matrix)
                except NotImplementedError as e:
                    print(str(e))
                    continue
            elif opcion == 'M':
                matrix = input_matrix(n)
                print_matrix(matrix)
            else:
                print("Opción no válida.")
                continue

            es_magico, suma_magica = is_magic_square(matrix)
            print(f"Constante mágica esperada: {suma_magica}")
            if es_magico:
                print("✅ ¡La matriz es un CUADRADO MÁGICO!")
            else:
                print("❌ La matriz NO es un cuadrado mágico.")

            print("-"*40)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()