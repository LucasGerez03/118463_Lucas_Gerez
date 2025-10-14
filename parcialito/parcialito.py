from colorama import Style, Fore, Back, init
import csv
import os
init(autoreset = True)

########################################################
# FUNCIONES DEL MENU
def imprime_error(msj=" "):
    print(Fore.RED + Style.BRIGHT +"=" * 80)
    print(Fore.RED + Style.BRIGHT + Back.BLACK +f"ERROR: {msj.upper()}")
    print(Fore.RED + Style.BRIGHT +"=" * 80)

def mostrar_menu():
    print(Fore.CYAN + Style.DIM + Back.LIGHTBLUE_EX +"=================Elija una Opción=================")
    print(Fore.CYAN + "1_Cargar Equipo")
    print(Fore.CYAN + "2_Mostrar equipos")
    print(Fore.CYAN + "3_Buscar equipo")
    print(Fore.CYAN + "4_Estadisticas")
    print(Fore.CYAN + "5_Filtrar Categoria")
    print(Fore.CYAN + "6_paso")
    print(Fore.CYAN + "7_Mostrar Informe")
    print(Fore.CYAN + "8_Salir")
    print(Fore.CYAN + "==================================================")


def continuar_menu():
    continuar = input(Fore.GREEN + "Desea continuar? (Y/N): ")
    if continuar.lower().strip() in ["n","no"]:
        print(Fore.GREEN + "gracias por usar el programa :D")
        return False
    elif continuar.lower().strip() in ["y","yes","s","si"]:
        return True
    else:
        imprime_error("OPCION INVALIDA, regresando al menu principal")
        return True

##############################################################################################
#OPCION 1

def cargar_equipos_a_lista(lista):
    n_equipos= int(input(Fore.CYAN + "Ingrese la cantidad de equipos a ingresar: "))
    for i in range(n_equipos):
        id = i+1
        nombre = input(Fore.CYAN + "ingrese un nombre al equipo: ")
        
        categoria = input(Fore.CYAN +"Ingrese una categoria (router, pc, notebook, impresora): ").lower().strip()
        while categoria not in ["pc","router","notebook","impresora"]:
            categoria = input(Fore.YELLOW + "Categoria invalida, intente una categoria valida(router, pc, notebook, impresora): ")
        
        estado = input(Fore.CYAN +"Ingrese un estado (funcional, fuera de servicio): ").lower().rstrip().lstrip()
        while estado not in ["funcional", "fuera de servicio"]:
            estado = input(Fore.YELLOW +"Estado invalido, ingrese un estado valido (funcional, fuera de servicio): ").lower().rstrip().lstrip()
        
        valor = float(input(Fore.CYAN + "ingrese un valor positivo: "))
        while valor < 0:
            valor = float(input(Fore.YELLOW + "Valor invalido, ingrese un valor positivo: "))

        equipo = {
            'id': id,
            'nombre': nombre,
            'categoria': categoria,
            'estado': estado,
            'valor': valor
        }
        lista.append(equipo)
    print(Fore.GREEN + "equipos cargados correctamente")


def escribir_y_leer_archivo(lista_equipos):
    with open("equipos.csv", "w" ,newline="", encoding="utf-8" ) as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["id", "nombre", "categoria", "estado", "valor"])
        writer.writeheader()
        for equipo in lista_equipos:
            writer.writerow(equipo)
    
    with open("equipos.csv", "r") as archivo2:
        reader = csv.DictReader(archivo2)
        for linea in reader:
            print(Fore.GREEN + f"{linea}")


def sobreescribir_y_leer_archivo(lista_equipos):
    with open("equipos.csv", "a" ,newline="", encoding="utf-8" ) as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["id", "nombre", "categoria", "estado", "valor"])
        for equipo in lista_equipos:
            writer.writerow(equipo)
    
    with open("equipos.csv", "r") as archivo2:
        reader = csv.DictReader(archivo2)
        for linea in reader:
            print(Fore.CYAN + f"{linea}")


def cargar_equipos(lista_de_equipos):
            if os.path.exists("equipos.csv"):
                print(Fore.LIGHTYELLOW_EX + "archivo existente")
                print(Fore.YELLOW + "1_reemplazar cambios")
                print(Fore.YELLOW + "2_agregar mas equipos")
                opcion = int(input(Fore.YELLOW +"desea reemplazar los cambios o agregar mas equipos?: " ))
                match opcion:
                    case 1:
                        cargar_equipos_a_lista(lista_de_equipos)
                        escribir_y_leer_archivo(lista_de_equipos)
                        return
                    case 2:
                        cargar_equipos_a_lista(lista_de_equipos)
                        sobreescribir_y_leer_archivo(lista_de_equipos)
            else: 
                cargar_equipos_a_lista(lista_de_equipos)
                escribir_y_leer_archivo(lista_de_equipos)


################################################################################################################
#OPCION 2
def mostrar_equipos(lista_equipos):
    for equipo in lista_equipos:
        print(Fore.CYAN + "=" * 80)
        linea_equipo = ""
        for clave in equipo:
            valor = equipo[clave]
            linea_equipo += f"{clave}: {valor} | " #Sacar la barrita
        linea_equipo = linea_equipo[:-3] #Elimino los ultimos 3 caracteres del equipo
        print(Fore.CYAN + linea_equipo)
    print(Fore.CYAN + "=" * 80)
#Validada
################################################################################################################
#opcion 3
def existe_clave_con_valor(clave="", valor="", lista_equipos=[]):
    for equipo in lista_equipos:
        if valor == equipo[f"{clave}"]:
            return True
    return False

def buscar_equipo_en(lista_equipos):
    nombre = input("ingrese el nombre del equipo a buscar: ").lower().strip()
    if existe_clave_con_valor("nombre",f"{nombre}",lista_equipos):
        for equipo in lista_equipos:
            if nombre == equipo["nombre"]:
                print(Fore.CYAN + f"{equipo}")
    else:
        print(Fore.YELLOW + f"No existe un equipo con el nombre {nombre}")

#Validada

################################################################################################################
# Opción 4.

def estadisticas(lista_equipos):
    print(Fore.CYAN + f"Total de equipos: {cant_total_equipos(lista_equipos)}")
    print(Fore.CYAN + f"Promedio general de valores: {promedio_valores(lista_equipos)}")
    print(Fore.CYAN + f"Cantidad de equipos 'fuera de servicio': {cant_fuera_de_servicio(lista_equipos)}")
    print(Fore.CYAN + f"Equipo mas caro: {equipo_con_mayor_valor(lista_equipos)}")
    print(Fore.CYAN + f"Equipo con menor valor: {equipo_con_menor_valor(lista_equipos)}")

def cant_total_equipos(lista_equipos):
    return len(lista_equipos)

def promedio_valores(lista_equipos):
    total = 0
    for equipo in lista_equipos:
        total += equipo["valor"]
    
    if total == 0:
        return 0
    else:
        return total / cant_total_equipos(lista_equipos)

def cant_fuera_de_servicio(lista_equipos):
    contador = 0
    for equipo in lista_equipos:
        if equipo["estado"] == "fuera de servicio":
            contador += 1
    return contador
    
def equipo_con_mayor_valor(lista_equipos):
    if not lista_equipos:
        return []
    mayor = lista_equipos[0]
    for equipo in lista_equipos:
        if mayor["valor"] <  equipo["valor"]:
            mayor = equipo
    return mayor

def equipo_con_menor_valor(lista_equipos):
    if not lista_equipos:
        return []
    menor = lista_equipos[0]
    for equipo in lista_equipos:
        if menor["valor"] >  equipo["valor"]:
            menor = equipo
    return menor


#Validada
################################################################################################################
#Opcion 5
def imprimir_matriz(matriz=[]):
    for fila in matriz:
        print(Fore.CYAN + f"{fila}")

def filtrar_categorias(lista_equipos=[]):
    if not lista_equipos:
        print(Fore.CYAN + "Lista Vacia")
        return
    categoria = input(Fore.CYAN + "Ingrese una categoria('pc','router','notebook','impresora'): ")
    lista = []
    for equipo in lista_equipos:
        if categoria == equipo["categoria"]:
            lista.append(equipo)
    imprimir_matriz(lista)

#Validada
#################################################################################################
#OPCION 6
def ordenamiento_de_lista(lista_de_equipos=[]):
    lista_copiada = lista_de_equipos.copy()
    n = len(lista_copiada)

    print(Fore.CYAN + "Como desea ordenar la lista?")
    print(Fore.CYAN + "1_Forma ascendente por valor")
    print(Fore.CYAN + "2_Forma descendente por valor")
    try:
        opcion = int(input(Fore.CYAN + "ingrese un numero: "))
        while opcion not in [1,2]:
            opcion = int(input(Fore.YELLOW + "ingrese un numero VALIDO: "))
    except ValueError:
        imprime_error("TIPO NO VALIDO")

    for i in range(n):
        for j in range(0, n - i - 1):
            if opcion == 1:
                # Orden ASCENDENTE: intercambiamos si el actual > siguiente
                if lista_copiada[j]['valor'] > lista_copiada[j + 1]['valor']:
                    lista_copiada[j], lista_copiada[j + 1] = lista_copiada[j + 1], lista_copiada[j]
            else:
                # Orden DESCENDENTE: intercambiamos si el actual < siguiente
                if lista_copiada[j]['valor'] < lista_copiada[j + 1]['valor']:
                    lista_copiada[j], lista_copiada[j + 1] = lista_copiada[j + 1], lista_copiada[j]
    imprimir_matriz(lista_copiada)


##################################################################################################
#Opcion 7
def generar_informe(lista_equipos):
    with open("informe.txt", "w" ,newline="", encoding="utf-8" ) as archivo:
        archivo.write("INFORME GENERAL DE INVENTARIO\n")
        archivo.write("-" * 29 + "\n")
        archivo.write(f"Equipos totales: {cant_total_equipos(lista_equipos)} \n")
        archivo.write(f"Promedio de valor: {promedio_valores(lista_equipos)}\n")
        archivo.write(f"Fuera de servicio: {cant_fuera_de_servicio(lista_equipos)}\n")
        archivo.write(f"Mas Caro: {equipo_con_mayor_valor(lista_equipos)}\n")
        archivo.write(f"Mas Barato: {equipo_con_menor_valor(lista_equipos)}\n")
        archivo.write("-" * 29 + "\n")

    with open("informe.txt", "r") as archivo:
        reader = archivo.readlines()
        for linea in reader:
            print(Fore.CYAN + linea)
#Validada


################################################################################################################

def programa():
    equipos = []
    flag = False
    while True:
        try:
            mostrar_menu()
            opcion = int(input(Fore.CYAN +"Ingrese una opcion (1-6): "))
            match opcion:
                case 1:
                    cargar_equipos(equipos)
                    flag = True
                case 2:
                    if flag:
                        mostrar_equipos(equipos)
                    else:
                        imprime_error("Ingresar a la opcion 1 antes de mostrar equipos")
                case 3:
                    buscar_equipo_en(equipos) 
                case 4:
                    estadisticas(equipos)
                case 5:
                    filtrar_categorias(equipos)
                case 6:
                    ordenamiento_de_lista(equipos)
                case 7:
                    if flag:
                        generar_informe(equipos)
                    else:
                        imprime_error("Ingresar a la opcion 1 antes de generar informe")
                case 8:
                    break
                case _:
                    imprime_error("Opcion incorrecta, porfavor seleccione una valida (1-6)")
            if continuar_menu():
                continue
            else:
                break
        except ValueError:        
            imprime_error("TIPO INVALIDO, la opcion elegida debe ser un numero en el rango 1-6. ")
programa()