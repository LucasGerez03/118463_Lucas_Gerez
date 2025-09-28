"""Mostrar la suma de los números pares desde el 1 hasta el 10."""
num = 1
suma = 0
while num <= 10:
    if num % 2 == 0 :
        suma += num
    num += 1
print(suma)

