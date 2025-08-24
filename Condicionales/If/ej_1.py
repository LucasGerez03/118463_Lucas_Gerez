"""A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
"""

altura = int(input("Ingrese una altura en Centimetros: "))
jugador = ""

if altura >= 200:
    jugador = "Ala-Pívot o Pívot"
elif altura >= 180:
    jugador = "Alero"
elif altura >= 160:
    jugador = "Escolta"
else:
    jugador = "Base"
    
print(f"el jugador seleccionado en base a la altura {altura} CM es: {jugador}")