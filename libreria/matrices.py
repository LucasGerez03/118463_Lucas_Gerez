def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial=0) -> list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        # matriz.append(fila)       
        matriz += [fila]
    return matriz

def cargar_matriz(matriz=[]):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i}, Columna {j}: "))

def imprimir_matriz(matriz=[]):
    for fila in matriz:
        print(fila)

def imprimir_matriz_con_end(matriz=[]):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()# <- este print vacío vuelve a la siguiente fila

def multiplicar_por_escalar(matriz, escalar):
    resultado = []
    for i in range(len(matriz)):
        nueva_fila = []
        for j in range(len(matriz[i])):
            nueva_fila.append(matriz[i][j] * escalar)
        resultado.append(nueva_fila)
    return resultado

matriz1 = [
    [1,2,3],
    [4,5,6]
]

# matriz1= inicializar_matriz(2,5)
# cargar_matriz(matriz1)

# imprimir_matriz_con_end(multiplicar_por_escalar(matriz1, 5))
# # cargar_matriz(ma_trix)
# imprimir_matriz(ma_trix)
