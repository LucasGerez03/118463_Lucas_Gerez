# Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …

num = int(input("ingrese un numero: "))
multiplicador = 0
while multiplicador <= 10 :
    print(f"{num} x {multiplicador} = {num * multiplicador} ")
    multiplicador += 1
    