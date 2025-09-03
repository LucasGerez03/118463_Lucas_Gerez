"""
Nivel Básico
1. Función que saluda a una persona

Enunciado:
Escribí una función que reciba un nombre y muestre un saludo personalizado. el nombre lo ingresa por consola
""" 

def saludar_persona(nombre: str) -> None:
    print(f"Hola, {nombre}! :) Bienvenido/a.")
    return

saludar_persona(input("Ingrese su nombre: "))


"""
Enunciado:
Escribí una función que reciba base y altura, y devuelva el área.
Datos por consola un argumento por defecto =10
"""
# #Todo###################################################
# def calcular_area(base: float = 10, altura: float = 10) -> float:
#     area = base * altura
#     print(f"El área del rectángulo es: {area}")
#     return 

# base = float(input("Ingrese la base del rectángulo (por defecto 10): "))
# altura = float(input("Ingrese la altura del rectángulo (por defecto 10): "))
# #Todo###################################################

# calcular_area(base, altura) # Valores ingresados 
# calcular_area()  # valores predeterminados con valores por defecto :p
# #Todo###################################################

# """Nivel Intermedio
# Función que devuelva suma, resta y multiplicación

# Enunciado:
# Escribí una función que reciba dos números y devuelva los tres resultados: suma, resta y multiplicación."""

# def operaciones_basicas(numero_1: float, numero_2: float) -> None:
# #!Documentacion    
#     suma = numero_1 + numero_2
#     resta = numero_1 - numero_2
#     multiplicacion = numero_1 * numero_2
    
#     print(f"los operadores son: {numero_1} y {numero_2}")
#     print(f"La suma es: {suma}")
#     print(f"La resta es: {resta}")
#     print(f"La multiplicación es: {multiplicacion}")
#     return
# ###Todo###################################################
# #?Entrada
# numero_ingresado_1 = float(input("Ingrese el primer número: "))
# numero_ingresado_2 = float(input("Ingrese el segundo número: "))
# resultados = operaciones_basicas(numero_ingresado_1, numero_ingresado_2)
"""
Enunciado:
Escribí una función que reciba cualquier cantidad de números y los multiplique los parametros por consola.

Ayuda: pedir al usuario cuantos numeros cargar, luego usar ese valor para iterar"""

def multiplicar_numeros(*args: float) -> None:
    resultado = 1   #? acumulador de cantidad total de la multiplicacion
    cantidad_numeros = int(input("¿Cuántos números deseas multiplicar? ")) #?Cant de ingresos    
    for numero_ingresado in range(cantidad_numeros):
        numero_ingresado = float(input(f"Ingrese un numero: "))
        resultado *= numero_ingresado
    print(f"El resultado de la multiplicación es: {resultado}")
    return

multiplicar_numeros()
            
   