
# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

negativos = 0
positivos = 0
cantidad_negativos = 0
cantidad_positivos = 0
maximo_positivo = None
total_ingresos = 0
continuar = "si"
while continuar == "si":
    num = int(input("Ingrese un número (positivo o negativo): "))
    total_ingresos += 1
    if num < 0:
        negativos += num
        cantidad_negativos += 1
    elif num > 0:
        positivos += num
        cantidad_positivos += 1
        if maximo_positivo is None or num > maximo_positivo:
            maximo_positivo = num
    continuar = input("¿Desea ingresar otro número? (si/no): ")
promedio_positivos = positivos / cantidad_positivos
porcentaje_negativos = (cantidad_negativos / total_ingresos) * 100

print(f"Suma acumulada de números negativos: {negativos}")
print(f"Suma acumulada de números positivos: {positivos}")
print(f"Cantidad de números negativos ingresados: {cantidad_negativos}")
print(f"Promedio de números positivos: {promedio_positivos}")
print(f"Número positivo más grande: {maximo_positivo}")
print(f"Porcentaje de números negativos ingresados respecto del total: {porcentaje_negativos}%")




