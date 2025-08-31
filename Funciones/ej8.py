#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

#TODO##############################################
#?SOLUCION 1
def maximo_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

#TODO##############################################
#?SOLUCION 2
def maximo_de_tres2(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    elif num3 > mayor:
        mayor = num3
    return mayor
#TODO##############################################

print(maximo_de_tres(0, 0, 0))
print(maximo_de_tres2(3, 7, 5))
