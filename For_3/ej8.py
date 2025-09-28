#Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

num = int(input("ingrese un numero: "))

if num >= 0 :  #Casos de positivos
    for i in range(1, num+1):
        for j in range(1 , i+1):
            print(f" {j} ", end="")
        print()
else:
    for i in range(-1, num-1, -1):   #Casos de Negativos
        for j in range(-1 , i-1, -1):
            print(f" {j} ", end="")
        print()


