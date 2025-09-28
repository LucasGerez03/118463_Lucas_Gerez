# 📌 Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar 
# el mercado.
# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)
# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)
# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


# 🔹 Requisitos del Programa
#  ✔️ Los datos deben solicitarse y validarse correctamente.
#  ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
#  ✔️ Presentar los resultados de manera clara y organizada.

TOTAL_EMPLEADOS = 10
contador = 0
nombre_masculino_mayor= ""
edad_mas_grande = 0
tecnologia_del_mayor = "" 

cant_no_voto_ia = 0
cant_voto_iot_ia = 0


while contador != TOTAL_EMPLEADOS:
    contador += 1
    
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad(+18): "))
    while edad < 18:
        edad = int(input("Porfavor ingrese una edad válida(+18): "))

    genero = input("Ingrese su Género(hombre/mujer): ")
    while genero != "hombre" and genero != "mujer":
        genero = input("Porfavor ingrese genero válido(hombre/mujer): ")

    tecnologia =  input("ingrese una tecnologia(IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RV/RA":
        tecnologia = input("Porfavor ingrese una tecnologia válida(IA, RV/RA, IOT): ")

    if genero == "hombre":
        match tecnologia:
            case "IOT":
                if (edad >= 25 and edad <= 50):
                    cant_voto_iot_ia += 1 
                if (edad >= 33 and edad <= 40):
                    cant_no_voto_ia += 1
            case "IA":
                if (edad >= 25 and edad <= 50):
                    cant_voto_iot_ia += 1

            case "RV/RA":
                if (edad >= 33 and edad <= 40):
                    cant_no_voto_ia += 1
        
        if edad > edad_mas_grande:
            edad_mas_grande = edad
            nombre_masculino_mayor = nombre
            tecnologia_del_mayor = tecnologia
    print(f"empleados ingresados hasta ahora({contador})")

porcentaje_no_votaron_ia = (cant_no_voto_ia / TOTAL_EMPLEADOS) * 100
print(f"""
    Empleados hombres que votaron por IOT/IA, entre 33 y 40 años: {cant_voto_iot_ia}.
    Empleados hombres que NO votaron por IA, entre 25 y 50 años es un porcentaje de: {porcentaje_no_votaron_ia}.
    El empleado hombre mas antiguo es {nombre_masculino_mayor} y su tecnologia votada fue {tecnologia_del_mayor}""")
    




