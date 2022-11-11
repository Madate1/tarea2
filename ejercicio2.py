
"""Crear una clase Perro con los mismos métodos y atributos del Gato, la particularidad es que este debe 
indicar en el método saludo, que es un perro y su sonido."""

class perro:
    especie = "Mi especie es Canis lupus"

    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido 

    def descripcion(self, raza):
        return f"Soy de raza {raza}"

    def saludo(self):
        return f"Soy {self.nombre} mi sonido es {self.sonido} "    

perro1 = perro("Steven","woooof")

print(perro1.saludo())
print(perro1.especie)
print(perro1.descripcion("Bulldog"))
