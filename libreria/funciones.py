def potencia(base, exponente):
    return base ** exponente

##########################################################
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
###########################################################
def maximo_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

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

#print(get_int("Ingrese un número entre 1 y 10: ", "Error, fuera de rango.", 1, 10, 1))

####################Recursividad####################
def calcular_factorial(numero:int) -> int:
    if numero == 0:   # caso base
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

######################################################
#------------------UNIDIMENSIONALES------------------------
######################################################
def crear_array(longitud:int, valor_inicial=0) -> list|None:
    try:
        array = [valor_inicial] * longitud
        return array    
    except TypeError:
        return None
    
##############################################################
def ingresar_numeros(cantidad:int) -> list|None:
    """Depende extrictamente de crear_array(longitud, valor)"""
    array = crear_array(cantidad)
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i+1}: "))
        array[i] = numero
    return array
##############################################################
def calcular_promedio_2(lista_num=[]) -> float|None:
    try: 
        return sum(lista_num)
    except (TypeError): #si está vacia o un error de tipo, retorna none
        return None

##############################################################
def producto_de_lista(lista_num=[]) -> float|None:
    if len(lista_num) == 0:   #si está vacia None
        return None
    producto = 1
    try:
        for numero in lista_num: 
            producto *= numero
        return producto
    except(TypeError):
        return None

###############################################################
def posicion_del_numero_maximo(lista_num=[]) -> int|None:
    if  len(lista_num) == 0 or type(lista_num) != list: #si no es una lista o si está vacia
        return None
    maximo = max(lista_num)   
    return lista_num.index(maximo)

################################################################
def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    """proposito: reemplazar nombres en una lista de nombres"""
    contador = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i].lower() == nombre_antiguo.lower():
            lista_nombres[i] = nombre_nuevo
            contador += 1      
    return contador


nombres = ["Ana", "Luis", "Ana", "Carlos", "Ana", "Ana"]
reemplazos = reemplazar_nombres(nombres, "aNa", "lukitas")
# print(nombres)
# print(f"Cantidad de reemplazos realizados: {reemplazos}")


################################################################

def interseccion_de_arrays(array_uno:list, array_dos: list) -> list|None:
    interseccion = []
    for num_lista_uno in array_uno:     #bucle primera lista
        for num_lista_dos in array_dos:     #compara todos los elementos de la segunda lista
            if num_lista_uno == num_lista_dos and num_lista_dos not in interseccion:
                interseccion.append(num_lista_dos)
    interseccion.sort() #ordeno la lista en orden ascendente
    return interseccion

# listorti_1= [1,2,4,3,5,6]
# listorti_2= [4,6,5,7,8,3,4,6,7,]
# print(interseccion_de_arrays(listorti_1, listorti_2))

################################################################
def union_entre_arrays(array_uno:list, array_dos:list) -> list|None :
    union = array_uno
    for numero in array_dos:
        if numero not in union:
            union.append(numero)
    return union  
# print(union_entre_arrays([1,2,3,4,5,6],[3,6,5,7,8,3,4,6,7,]))
################################################################
def diferencia_entre_arrays(array_1:list, array_2:list)-> list|None:
    diferencia = []
    for numero in array_1:
        if numero not in array_2 and numero not in diferencia:
            diferencia.append(numero)
    return diferencia
    
# listorti_1= [1,2,3,4,5]
# listorti_2= [3,4,5,6,7]
# print(diferencia_entre_arrays(listorti_1, listorti_2))