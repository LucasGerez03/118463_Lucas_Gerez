# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

continuar = "si"
ingresos = 0
suma = 0
promedio = 0
while ingresos <= 10 and continuar == "si":
    numero = int(input("ingrese un numero: "))
    suma += numero
    ingresos += 1
    continuar = input("desea continuar? (si/no): ")

promedio = suma / ingresos

print(f"suma total: {suma}")
print(f"promedio total: {promedio}")

