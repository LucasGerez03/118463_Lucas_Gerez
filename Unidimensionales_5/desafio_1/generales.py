from especificas import esta_entre, es_positivo

def mostar_msg():
    print("=============================================")
    print("Opciones del Menú:")
    print("1-Ingresar datos")
    print("2-Cantidad de positivos y negativos")
    print("3-Suma de los números pares")
    print("4-Mayor número impar")
    print("5-Listar los números ingresados")
    print("6-Listar los números pares")
    print("7-Listar los números en posiciones impares")
    print("8-Salir")
    print("=============================================")
    
def ingresar_numeros(): #validacion de la lista
    lista= []
    ingresos_restantes = 10
    while ingresos_restantes > 0:
        print(f"RESTANTES: {ingresos_restantes}\n====================================================")
        try:    
            numero = int(input("Ingrese un numero: ")) 
            if esta_entre(numero,-1000, 1000): #verificar el ingreso en rango
                lista += [numero]
                ingresos_restantes -= 1
            else:
                print("ERROR al ingresar un numero, el rango asignado es de: (-1000 hasta 1000)")
        except ValueError:
            print("ERROR DE INGRESO DE DATO, solo se admiten numeros")
    return lista


# print(ingresar_numeros())

# def ingresar_numeros(): #validacion de la lista
#     lista= []
#     for i in range(10):
#         numero = int(input("Ingrese un numero: ")) 
#         if esta_entre(numero,-1000, 1000): #verificar el ingreso en rango
#             lista += [numero]
#         else:
#             print("ERROR al ingresar un numero, el rango asignado es de: (-1000 hasta 1000)")
#             numero = int(input("Porfavor ingrese un numero valido:")) 
#             while not esta_entre(numero, -1000, 1000): #repetir bucle hasta un ingreso valido
#                 numero = int(input("Porfavor ingrese un numero valido:"))
#             lista += [numero] #ingresar el numero valido
#     return lista


def cant_positivos_y_negativos(lista=[]):
    positivos= []
    negativos= []
    cant_pos = 0
    cant_neg = 0
    for numero in lista:
        if es_positivo(numero):
            positivos+= [numero]
            cant_pos+= 1
        else:
            negativos+= [numero]
            cant_neg+=1
    return f"-Cant. Negativos: {cant_neg}\n-Cant. Positivos: {cant_pos}\n-Lista Negativos: {negativos} \n-Lista Positivos: {positivos}"
