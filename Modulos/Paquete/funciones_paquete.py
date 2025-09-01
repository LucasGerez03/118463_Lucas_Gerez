def es_par_o_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")


#!##############################################################
# Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
# En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive)
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

# En caso de que la función no haya podido conseguir un número válido, la misma retorna None.


def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    num = int(input(mensaje)) 
    while num < minimo or num > maximo: 
        reintentos -= 1
        if reintentos <= 0:   
            return None     #fin de reintentos 
        print(mensaje_error)
        num = int(input(mensaje))
    return num  #fin del bucle

print(get_int("Ingrese un número entre 1 y 10: ", "Error, fuera de rango.", 1, 10, 1))

####################?Recursividad####################
def calcular_factorial(numero:int) -> int:
    if numero == 0:   # caso base
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

#print(calcular_factorial(5))  # 120


