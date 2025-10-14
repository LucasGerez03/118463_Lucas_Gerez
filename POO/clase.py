# Este es un gran momento para practicar y crear una clase para trabajar con una **Persona**. Agregarle **3 atributos de instancia**, por lo menos** 2 de clase**, el **constructor y dos métodos (uno con parámetros y otro sin parámetro). **

# **Luego instanciar a dos personas y mostrarlas por consola. **

class Persona:
    especie = "Humano"
    residencia = "Avellaneda"
    hincha_de = "River plate"

    def __init__(self, nombre, edad, estado_civil):
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil

    def saludar(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años y vivo en {self.residencia}")
        



# class Persona:
#     def __init__(self, nombre, edad, genero):
#         # Atributos de instancia
#         self.nombre = nombre
#         self.edad = edad
#         self.genero = genero

#     def saludar(self):
#         return f"Esto es un saludo y mi nombre es: {self.nombre}."

#     def cumplir_anios(self, anios):
#         self.edad += anios
#         return f"{self.nombre} tiene {self.edad} anios."

# # Aca instancio dos personas X
# persona1 = Persona("Pepe", 30, "Masculino")
# persona2 = Persona("Miriam", 25, "Femenino")

# # Muestro data por consola
# print(persona1.saludar())
# print(persona2.saludar())
# print(persona1.cumplir_anios(5))
# print(persona2.cumplir_anios(3))


###########################################################

# Crear una clase Atleta, que tenga su nombre, apellido, altura,  peso, teléfono e índice de masa corporal (descripción) . Decidir que atributos deben ser públicos y cuales privados. Crear los métodos get y set que crea necesarios.

# Donde el imc es es peso dividido, la altura al cuadrado. con la altura en metros.

class Atleta:
    def __init__(self, nombre, apellido, telefono, altura, peso):
        self.nombre = nombre        
        self.apellido = apellido    
        self.telefono = telefono

        self._altura = altura
        self._peso = peso
        self._imc = self._calcular_indice_masa_c()

    def calcular_indice_masa_c(self):
        if self._altura > 0:
            valor = self._peso / (self._altura ** 2)
            return round(valor, 2)
        return 0.0