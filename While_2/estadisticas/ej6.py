"""Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
 Calcular la suma de los números ingresados y el promedio de los mismos."""

continuar = "si"
num = 0
suma = 0
promedio = 0
ingresos = 0

while continuar == "si":
    num = int(input("ingrese un numero: "))
    suma += num
    ingresos += 1
    continuar = input("¿Desea ingresar otro número? (si/no): ")

promedio = suma / ingresos

print (f"La suma de los números ingresados es: {suma}, y su promedio de {promedio}")