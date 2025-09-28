"""Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
 Mostrar la suma y el promedio por pantalla."""

ingresos = 0
suma = 0
promedio = 0
while ingresos < 5:
    num = int(input("Ingrese un número: "))
    suma += num
    ingresos += 1

promedio = suma / ingresos
print(f"La suma de los números ingresados es: {suma} y su promedio {promedio}")