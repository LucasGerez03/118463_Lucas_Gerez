# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

def calcular_promedio(lista_num=[]) -> float|None:
    try: 
        promedio = 0
        contador = 0
        for numero in (lista_num):
            promedio += numero 
            contador += 1
        return promedio / contador
    except (TypeError, ZeroDivisionError): #si está vacia o un error de tipo, retorna none
        return None


####################forma 2 #############################
def calcular_promedio_2(lista_num=[]) -> float|None:
    try: 
        return sum(lista_num)
    except (TypeError): #si está vacia o un error de tipo, retorna none
        return None
    

