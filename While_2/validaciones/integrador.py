# Integrador Validaciones
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.


apellido = input("Ingrese su apellido: ")
while apellido == "":
    apellido = input("Porfavor ingrese un apellido válido: ")

edad = int(input("ingrese una edad entre 18 y 90 años: "))
while edad > 90 or edad < 18:
    edad = int(input("porfavor ingrese una edad válida: "))

estado_civil = input("ingrese un estado civil (soltero/casado/viudo): ")
while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "viudo" :
    estado_civil = input("Porfavor ingrese un estado civil válido (soltero/casado/viudo): ")

numero_legajo = int(input("ingrese un legajo: "))

while numero_legajo < 1000 or numero_legajo > 9999:
    numero_legajo = int(input("Porfavor ingrese un legajo válido: "))

print(f"Apellido ingresado: {apellido}")
print(f"Edad: {edad}")
print(f"Estado Civil: {estado_civil}")
print(f"Numero de Legajo: {numero_legajo}")



