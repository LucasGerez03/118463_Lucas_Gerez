""" Conversor de monedas

Escribir un programa que pida al usuario un monto en dólares y lo convierta a pesos argentinos y a euros. Usar funciones para cada conversión y mostrar el resultado con dos decimales. """


def dolares_a_pesos(dolares: int, tasa_cambio=1400) -> float:
    return dolares * tasa_cambio
    

def dolares_a_euros(dolares: int, tasa_cambio=0.85) -> float:
    return dolares * tasa_cambio
    

monto_dolares = float(input("Ingrese monto en dolares a covertir: "))
monto_pesos = dolares_a_pesos (monto_dolares)
monto_euros = dolares_a_euros  (monto_dolares)


print("#Conversor de divisas")
print(f"Su monto en pesos argentinos es: ${monto_pesos:.2f}")
print(f"Su monto en euros es: €{monto_euros:.2f}")




""" 
Calculadora geométrica
Crear un programa que permita al usuario elegir una figura geométrica (cuadrado, rectángulo, triángulo, círculo) mediante un menú. Luego, calcular su área y perímetro usando funciones específicas para cada caso.

TODOS LOS RETURN VAN A DEVOLVER  (AREA, PERIMETRO)
 """

import math

def cuadrado(lado:float) -> float: 
    """ return: (area, perimetro) """
    return lado**2, lado * 4


def rectangulo(base: float, altura: float) -> float: 
    """ return: (area, perimetro) """
    return base * altura, 2 * (base  +  altura) #YEPEEEEE


def triangulo(base : float, altura : float) -> float:
    """ return: (area, perimetro) """
    area = (base * altura) / 2 
    perimetro = base + altura + math.sqrt(base**2 + altura**2)
    return area, perimetro
    

def circulo(radio: float) -> float:
    """ return: (area, perimetro) """
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio 
    return area, perimetro

# figura_geometrica = input("que figura desea saber su area y perimetro?: ").lower()
# match figura_geometrica:
#     case "rectangulo":
#         base = float(input("ingrese la base del rectangulo: "))
#         altura = float(input("ingrese la altura del rectangulo: "))
#         area, perimetro = rectangulo(base, altura)
#     case "cuadrado":
#         lado = flo(tinput("ingrese un lado del rectangulo"))

# area , permiimetro = cuadrad        
#     case "triangulo":
#         base = input("Ingrese la base del triangulo: ")
#         altura = input("Ingrese la altura)
#         base, altura =
#         pass
#     case "circulo":
#         pass

# print(f"el area del {figura_geometrica} es {area} y su perimetro es {perimetro}")

# """ 
# Gestor de notas de alumnos
# El programa debe pedir el nombre de un alumno y sus 3 notas. Usando una función, calcular el promedio y mostrar si aprobó o desaprobó (mínimo 6). Guardar los resultados en un diccionario {nombre: promedio}.
# #funcion
# """
    
# nombre = input("Ingrese el nombre del alumno: ")
# notas = []
# for i in range (3):
#     nota = float(input(f"Ingrese su nota {i+1}"))
#     nota.append(nota)

# # }:)




"""
Juego del número secreto
Generar un número aleatorio entre 1 y 100. El usuario debe adivinarlo. El programa debe dar pistas ("más alto", "más bajo") hasta que acierte. Llevar un contador de intentos y mostrarlo al final.
"""
import random
def juego_numero_secreto():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    print("Existe un numero secreto, ¿podes adivinar cual es?")

    while not adivinado :
        intento = int(input("Introduce un numero"))
        intentos += 1
        
        if intento < numero_secreto:
            print("Mas alt!")
        
    pass





"""
Calculadora de factorial con recursividad
Implementar una función recursiva que calcule el factorial de un número entero positivo ingresado por el usuario.
 Comparar el resultado con la versión iterativa.
"""

# def factorial_recursivo(numero: int) -> int:
#     if numero == 0 or numero == 1:
#         return 1
#     else:
#         return numero * factorial_recursivo(numero - 1)
    
# print(factorial_recursivo(6))

# # }:)

"""
Gestión de inventario simple
Simular un inventario con un diccionario de productos y precios. Permitir:
Agregar productos
Eliminar productos
Listar productos
Calcular el total del inventario.
Usar un menú con match-case o if-elif.
"""



 




"""
Validador de contraseñas
Escribir una función que valide contraseñas según estas reglas:
Mínimo 8 caracteres
Al menos una mayúscula
Al menos un número
Al menos un carácter especial (!@#$%&*).
Probar la función con varias entradas.
"""


def validar_contra(contrasena):
    pass



"""
Conversor de temperaturas modularizado
Crear un módulo conversores.py que tenga funciones para convertir:
Celsius ↔ Fahrenheit
Celsius ↔ Kelvin
Importar el módulo en otro archivo principal y probarlo.
"""




"""
Simulación de cajero automático
Hacer un programa que pida un PIN para acceder. Luego permitir:
Consultar saldo
Depositar dinero
Retirar dinero (si hay saldo suficiente).
Usar funciones para cada acción y estructuras de control.
"""






"""
Control de versiones simulado
Crear un programa que simule algunos comandos básicos de Git:
init → iniciar repositorio
add <archivo> → agregar archivo
commit <mensaje> → guardar cambios
status → mostrar estado actual.
Usar un diccionario para guardar el estado de los archivos y funciones para cada comando.
"""

# #Diccionario
# repositorio={
#     "Inicializador"=False
#     "Archivos" ={}
#     "commit"=[]
# }
# def Init()
#     "Inicializador"=True
#     print("Repositor Iniciado")

# def Add()
#     if "Inicializador"=False
#         print("")
