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






def ingresar_recaudacion(matriz_colectivos):
        
        #Ingreso la linea y coche y verifico que exista
        bandera = False
        while not bandera:
            try:
                num_linea = int(input("Ingrese el numero de su linea: ")) 
                num_coche = int(input("Ingrese el numero de su coche: "))
                if esta_la_linea(num_linea, matriz_colectivos) and esta_el_coche(num_coche, matriz_colectivos):
                    bandera = True
                else:
                    print("================================================")
                    print("ERROR: Linea o Coche NO encontrado/a")
                    print("================================================")
            except ValueError:
                print("================================================")
                print("ERROR DE TIPO: LINEA o COLECTIVO no válido")
                print("================================================")


        indice_linea = num_linea - 1

        for j in range(len(matriz_colectivos[indice_linea])): #si tengo la linea, solo busco en esa linea NO en toda la matriz
            if matriz_colectivos[indice_linea][j] == num_coche:
                bandera = False
                while not bandera:    
                    try:    
                        recaudacion = float(input("Ingrese la recaudacion: $")) #ingreso recaudacion
                        if recaudacion >= 0:
                            matriz_recaudacion[indice_linea][j] += recaudacion
                            bandera = True # reemplazo en la matriz recaudacion
                            print(f"=======Recaudacion realizada con exito=======")
                        else:
                            print("================================================")
                            print("ERROR: Recaudacion debe ser POSITIVO")
                            print("================================================")
                    except ValueError:
                        print("======ERROR DE TIPO: Recaudacion DEBE ser un NUMERO ENTERO======:")

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

# ingresar_recaudacion(matriz_coches)
# print(matriz_recaudacion)
#########################################################
#OPCION 2

def mostrar_recaudacion_de_coches(matriz_recaudacion, matriz_colect):
    for linea in range(len(matriz_recaudacion)):
        print(f"=================LINEA: {linea + 1}=================")
        for coche in range(len(matriz_recaudacion[linea])):
            print(f"Coche: {matriz_colect[linea][coche]}\nRecaudacion: {matriz_recaudacion[linea][coche]}")
            print(" ")
    print("==========================================")

# mostrar_recaudacion_de_coches(matriz_recaudacion, matriz_coches)

#########################################################
#OPCION 3

def calcular_y_mostrar_recaudacion_por_linea(matriz_recaudacion):
    for linea in matriz_recaudacion:
        recaudacion = sum(linea)
        print(f" \nRecaudacion de linea {matriz_recaudacion.index(linea) + 1}: {recaudacion}\n ")

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




#########################################################
#OPCION 1

def cargar_planilla_recaudacion(matriz_chofer, matriz_coches): 
        bandera_1 = False
        while not bandera_1: 
            try:    
                legajo = int(input("Porfavor ingrese su legajo: "))
                if es_chofer_valido(legajo, matriz_chofer):
                    bandera_1 = True      
                else:                    
                    print("=========================================================")
                    print(f"ERROR: Legajo {legajo} NO encontrado, reintentar")
                    print("=========================================================")
            except ValueError:
                print("=========================================================")
                print(f"ERROR DE TIPO: Legajo debe ser un numero de 6 digitos")
                print("=========================================================")
        ingresar_recaudacion(matriz_coches)
    
def es_chofer_valido(legajo_chofer, matriz_chofer):
    for i in range(len(matriz_chofer)):
        for j in range(len(matriz_chofer[i])):
            if matriz_chofer[i][j] == legajo_chofer: 
                return True
    return False

# cargar_planilla_recaudacion(matriz_chofer, matriz_coches)
# print(matriz_recaudacion1)



##########################################
#PROGRAMA


opcion = None
while opcion != 6:
    try:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion (1-6): "))
        match opcion:
            case 6:
                break
            case 1:
                cargar_planilla_recaudacion(matriz_chofer, matriz_coches)
            case 2:
                mostrar_recaudacion_de_coches(matriz_recaudacion, matriz_coches)
            case 3:
                calcular_y_mostrar_recaudacion_por_linea(matriz_recaudacion)
            case 4:
                calcular_y_mostrar_recaudacion_de_coche(matriz_coches, matriz_recaudacion)
            case 5:
                calcular_y_mostrar_total_recaudacion(matriz_recaudacion)
            case _:
                print("Opcion incorrecta, porfavor seleccione una valida (1-6)")

        continuar = input("Desea continuar? (Y/N): ")
        if continuar.lower() == "n":
            break
    except ValueError:        
        print("ERROR DE TIPO: la opcion elegida debe ser un numero en el rango 1-6. ")     