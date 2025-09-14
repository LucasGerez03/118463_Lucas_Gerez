from validate import *
# Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):


def get_string(longitud:int) -> str|None:
    string= input(f"Ingrese una cadena de texto con {longitud} caracteres: ")
    while validate_length(longitud, string) == False:
        string = str(input(f"Ingrese una cadena de texto con {longitud} caracteres: "))
    return string

print(get_string(3))