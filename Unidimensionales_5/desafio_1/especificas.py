from generales import esta_entre

def mostar_msg():
    print("Opciones del Menú:")
    print("1-Ingresar datos")
    print("2-Cantidad de positivos y negativos")
    print("3-Suma de los números pares")
    print("4-Mayor número impar")
    print("5-Listar los números ingresados")
    print("6-Listar los números pares")
    print("7-Listar los números en posiciones impares")
    print("8-Salir")

def ingresar_numeros(): #validacion de la lista
    lista= []
    for i in range(10):
        numero = int(input("Ingrese un numero: ")) 
        if esta_entre(numero,-1000, 1000): #verificar el ingreso en rango
            lista += [numero]
        else:
            print("ERROR al ingresar un numero, el rango asignado es de: (-1000 hasta 1000)")
            numero = int(input("Porfavor ingrese un numero valido:")) 
            while not esta_entre(numero, -1000, 1000): #repetir bucle hasta un ingreso valido
                numero = int(input("Porfavor ingrese un numero valido:"))
            lista += [numero] #ingresar el numero valido
    return lista