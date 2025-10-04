# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma = 0
contador = 0
for i in range(10):
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Suma: {suma}, Promedio: {promedio}")
else:
    print("No se ingresaron números.")

