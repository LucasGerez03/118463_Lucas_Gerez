# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def calcular_promedio_positivos(lista_num=[]) -> float|None :
    """"""
    try: 
        promedio = 0
        contador = 0
        for numero in (lista_num):
            if numero > 0:
                promedio += numero 
                contador += 1
        return promedio / contador
    except (TypeError, ZeroDivisionError): #si está vacia o un error de tipo, retorna none
        return None
    
print(calcular_promedio_positivos([5,5,5,5-4]))
print(calcular_promedio_positivos([2,-2,3,3]))
print(calcular_promedio_positivos([]))
print(calcular_promedio_positivos(["asdff"]))
    

