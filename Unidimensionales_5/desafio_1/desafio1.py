
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

ingreso_numeros= False
numeros_lista= []
while True:
    mostar_msg()
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            numeros_lista += ingresar_numeros()
            ingreso_numeros= True 
        case 2:
            if ingreso_numeros:
                print(cant_positivos_y_negativos(numeros_lista))
            else:
                print("Ingresar numeros antes de acceder a esta opcion")
        case 3:
            print(f"la suma total de los numeros pares de la lista es:{sumar_pares_de_lista(numeros_lista)}")
        case 4:
            print(f"mayor numero impar de la lista {print(mayor_numero_impar(numeros_lista))}")
        case 5:
            mostrar_lista_en_orden(numeros_lista)
        case 6:
            mostrar_numeros_pares(numeros_lista)
        case 7:
            if not ingreso_numeros:
                print("Ingresar numeros antes de acceder a esta opcion")
            else:
                mostrar_numeros_en_pos_impares(numeros_lista)

        case 8:
            print(f"Gracias por usar el programa, Adios")
            break

    print("desea continuar?: ")
    respuesta = input("Y/N: ")
    if respuesta.lower() == "y":
        continue
    else:
        print(f"Gracias por usar el programa, Adios :D")
        break


