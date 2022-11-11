
"""Crear una clase Gato que tenga 2 atributos, nombre y sonido. También agregar un método que permita saludar, 
en este método indicar que clase es a la que pertenece y cual es su sonido."""

class gato:
    especie = "Mi especie es Asiática"

    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido 

    def descripcion(self, raza):
        return f"Soy de raza {raza}"

    def saludo(self):
        return f"Soy {self.nombre} mi sonido es {self.sonido}"    

gato1 = gato("Nieves","miau")

print(gato1.saludo())
print(gato1.especie)
print(gato1.descripcion("Burmés"))


