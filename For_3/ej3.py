# Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

num = int(input("ingrese un numerin: "))

if num >= 0:
    for i in range(0 , num+1):
        print(i)
else:
    for i in range(0 , num-1 , -1):
        print(i)
        