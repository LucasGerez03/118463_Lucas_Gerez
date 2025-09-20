def es_par_o_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")


####################Validación de datos####################

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    num = int(input(mensaje)) 
    while num < minimo or num > maximo: 
        reintentos -= 1
        if reintentos <= 0:   
            return None     #fin de reintentos 
        print(mensaje_error)
        num = int(input(mensaje))
    return num  #fin del bucle

# print(get_int("Ingrese un número entre 1 y 10: ", "Error, fuera de rango.", 1, 10, 1))

####################Recursividad####################
def calcular_factorial(numero:int) -> int:
    if numero == 0:   # caso base
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

#print(calcular_factorial(5))  # 120


######################################################
def crear_array(longitud:int, valor_inicial=0) -> list|None:
    try:
        array = [valor_inicial] * longitud
        return array    
    except TypeError:
        return None
    
##############################################################
def ingresar_numeros(cantidad:int) -> list|None:
        array = crear_array(cantidad)
        for i in range(cantidad):
            numero = int(input(f"Ingrese el número {i+1}: "))
            array[i] = numero
        return array
