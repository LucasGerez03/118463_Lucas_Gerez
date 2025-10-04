
# 📌 Desafío: Menú de Opciones con Listas y Funciones
# Desarrollar un programa en Python que presente un menú de opciones donde el usuario pueda realizar distintas operaciones con un conjunto de números.
# 🔹 Opciones del Menú:
#  1️⃣ Ingresar datos: Permitir al usuario ingresar 10 números enteros en el rango de -1000 a 1000.
#  2️⃣ Cantidad de positivos y negativos: Mostrar cuántos números ingresados son positivos y cuántos son negativos.
#  3️⃣ Suma de los números pares: Calcular y mostrar la sumatoria de los números pares.
#  4️⃣ Mayor número impar: Identificar y mostrar el mayor número impar ingresado.
#  5️⃣ Listar los números ingresados: Mostrar todos los números en el orden en que fueron ingresados.
#  6️⃣ Listar los números pares: Mostrar únicamente los números pares de la lista.
#  7️⃣ Listar los números en posiciones impares: Mostrar los números que se encuentran en posiciones impares dentro de la lista.
#  8️⃣ Salir del programa.
# 🔹 Condiciones:
#  ✔️ El usuario debe ingresar los números antes de acceder a las opciones 2 a 7.
#  ✔️ El programa debe estar estructurado en funciones, siguiendo el paradigma de programación funcional:
# Funciones específicas: Para operaciones como determinar si un número es positivo, negativo o par.
# Funciones generales: Para listar elementos o calcular sumatorias.
# 🔹 Estructura del Código:
#  📌 El programa debe estar organizado en módulos:
# Especificas.py: Contendrá las funciones específicas.
# Array_Generales.py: Contendrá las funciones generales.
# Las funciones de entrada de datos deben importarse desde el módulo   .
# 🔹 Consejo:
#  ✅ Desarrollar y probar primero cada función individualmente antes de organizarlas en módulos.

from especificas import *
from generales import *

# mostar_msg()
# print(esta_entre(1,10,20))
# print(es_positivo(-1))
# ingresar_numeros()

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
    return f"-Cant. Negativos: {cant_neg}\nCant. Positivos: {cant_pos}\nLista Negativos: {negativos} \n Lista Positivos: {positivos}"

def sumar_pares_de_lista(lista=[]):
    total = 0
    for numero in lista:
        if es_par(numero):
            total += numero
        else:
            continue
    return total

print(sumar_pares_de_lista([5,-2,-7,-8,12]))
# print(cant_positivos_y_negativos([]))

# while True:
#     mostar_msg()
#     opcion = int(input("ingrese una de las opcioens 1-8: "))

# mostar_msg()