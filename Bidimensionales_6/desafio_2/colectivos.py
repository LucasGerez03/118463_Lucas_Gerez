# 📌 Desafío: Gestión de Recaudaciones en una Empresa de Colectivos
# Una empresa de transporte cuenta con 3 líneas de colectivos, cada una con 5 coches, lo que da un total de 15 unidades en circulación. La empresa emplea 15 choferes, cada uno identificado con un legajo único generado aleatoriamente.
# Para llevar un control eficiente de la recaudación diaria, se necesita desarrollar un software que permita gestionar y analizar los ingresos obtenidos por cada línea y coche.
# 🔹 Funcionalidades del Programa
# El sistema debe presentar un menú de opciones con las siguientes funciones:
# 1️⃣ Cargar planilla de recaudación
# El chofer debe identificarse ingresando su número de legajo.
# Se debe validar que el legajo ingresado exista dentro de la matriz de legajos generada previamente.
# Si el chofer existe, podrá ingresar la recaudación indicando la línea y el coche en el que realizó el viaje.
# Un chofer puede cargar múltiples recaudaciones por día, en distintas líneas y coches.
# Cada coche dentro de cada línea puede acumular varias recaudaciones diarias.
# 2️⃣ Mostrar la recaudación de cada coche y línea
# Presentar una matriz con la recaudación total de cada coche en cada línea.
# 3️⃣ Calcular y mostrar la recaudación por línea
# Sumar y mostrar la recaudación total de cada línea de colectivos.
# 4️⃣ Calcular y mostrar la recaudación por coche
# Permitir al usuario seleccionar un coche y mostrar la suma total de su recaudación.
# 5️⃣ Calcular y mostrar la recaudación total
# Mostrar el total general de todas las recaudaciones registradas.
# 6️⃣ Salir del programa


# 🔹 Requisitos del Desarrollo
# ✔️ Modularización:
# El programa debe estar organizado en múltiples funciones, incluyendo:
# Ingreso de datos
# Validación de líneas y coches
# Generación y verificación de existencia de legajo
# Cálculos de recaudaciones
# ✔️ Validaciones:
# El legajo ingresado debe existir en la matriz de legajos.
# La línea y el coche seleccionados deben ser válidos.
# No debe permitirse el ingreso de valores negativos o inválidos en la recaudación.

def mostrar_menu():
    print("==================Elija una Opción=================")
    print("1_Cargar planilla de recaudación")
    print("2_Mostrar la recaudacion de cada coche y línea")
    print("3_Calcular y mostrar la recaudación por línea")
    print("4_Calcular y mostrar la recaudacion por coche")
    print("5_Calcular y mostrar la recaudacion total ")
    print("6_Salir del programa")
    print("===================================================")


matriz_chofer = [
    [111,222,333],
    [444,555,666],
    [777,888,999]
]

matriz_coches = [
    [777, 456, 789],
    [321, 777, 987],
    [000, 900, 777]
]

matriz_recaudacion = [
    [1.5, 1.5, 0],
    [0, 1.5, 0],
    [1.5, 0, 1.5]
]

matriz_recaudacion1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 1.5]
]


#########################################################
#OPCION 1

def cargar_planilla_recaudacion(): 
    try:
        legajo = int(input("Porfavor ingrese su legajo: "))
        if not es_chofer_valido(legajo):      
                print("Legajo NO encontrado o Inválido, reintentar")
                legajo = int(input("legajo: "))
                # print("Su legajo debe constar de 6 numeros")
        ingresar_recaudacion(matriz_coches)
        pass
    except:
        pass
    
    
def es_chofer_valido(legajo_chofer, matriz_chofer):
    for i in range(len(matriz_chofer)):
        for j in range(len(matriz_chofer[i])):
            if matriz_chofer[i][j] == legajo_chofer: 
                return True
    return False



def ingresar_recaudacion(matriz_colectivos):
    try:    
        num_linea = int(input("Ingrese el numero de su linea: ")) 
        num_coche = int(input("Ingrese el numero de su coche: "))
        
        while not esta_la_linea(num_linea, matriz_colectivos) or not esta_el_coche(num_coche, matriz_colectivos):
            print("==============ERROR==============\nLinea o Coche NO encontrado/a")
            num_linea = int(input("Ingrese un numero de linea valido: ")) 
            num_coche = int(input("Ingrese un numero de coche valido: "))

        indice_linea = num_linea - 1
        encontrado = False

        for j in range(len(matriz_colectivos[indice_linea])): #si tengo la linea, solo busco en esa linea NO en toda la matriz
            if matriz_colectivos[indice_linea][j] == num_coche:
                recaudacion = float(input("Ingrese la recaudacion: $")) #ingreso recaudacion
                matriz_recaudacion[indice_linea][j] += recaudacion # reemplazo en la matriz recaudacion
                print(f"recaudacion reemplazada con exito") 
                encontrado = True
                break
    except ValueError:
        print("LINEA o COLECTIVO no válido")

def esta_la_linea(num, matriz):
    flag = False
    for linea in matriz:
        if matriz.index(linea) + 1 == num:  #si el indice de linea +1 es igual a la linea buscada, cambia la flag
            flag = True
    return flag

def esta_el_coche(num, matriz):
    flag = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num:
                flag = True
                break
        if flag:
            break
    return flag

ingresar_recaudacion(matriz_coches)
print(matriz_recaudacion)
#########################################################
#OPCION 2

def mostrar_recaudacion_de_coches(matriz_recaudacion, matriz_colect):
    for linea in range(len(matriz_recaudacion)):
        print(f"=================LINEA: {linea + 1}=================")
        for coche in range(len(matriz_recaudacion[linea])):
            print(f"Coche: {matriz_colect[linea][coche]}\nRecaudacion: {matriz_recaudacion[linea][coche]}")
            print("**************************************")
    print("==========================================")

# mostrar_recaudacion_de_coches(matriz_recaudacion, matriz_coches)

#########################################################
#OPCION 3

def calcular_y_mostrar_recaudacion_por_linea(matriz_recaudacion):
    for linea in matriz_recaudacion:
        recaudacion = sum(linea)
        print(f"Recaudacion de linea {matriz_recaudacion.index(linea) + 1}: {recaudacion}")

#calcular_y_mostrar_recaudacion_por_linea(matriz_recaudacion)

###########################################################
#OPCION 4

def calcular_y_mostrar_recaudacion_de_coche(matriz_colect, matriz_recaudacion):
    try:
        total = 0
        coche = int(input("Ingrese un coche : "))
        for i in range(len(matriz_colect)):
            for j in range(len(matriz_colect[i])):
                if matriz_colect[i][j] == coche:
                    total += matriz_recaudacion[i][j]
        if total > 0:
            print(f"La recaudacion total del coche {coche}: ${total}")
        else:
            print(f"coche {coche} invalido o sin recaudacion")
    except ValueError:
        print("***ERROR*** Valor ingresado no valido, ingresar un numero de coche válido")

# calcular_y_mostrar_recaudacion_de_coche(matriz_coches, matriz_recaudacion)

###########################################################
#OPCION 5

# 5️⃣ Calcular y mostrar la recaudación total
# Mostrar el total general de todas las recaudaciones registradas.

def calcular_y_mostrar_total_recaudacion(matriz_recaudacion):
    total = 0
    for linea in matriz_recaudacion:
        total += sum(linea)
    print(f"Total de Recaudacion en todas las lineas y coches: ${total}")
    
# calcular_y_mostrar_total_recaudacion(matriz_recaudacion)




