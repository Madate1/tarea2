#Herencia entre gato y perro

class mascotas:
    
     def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido 
    
     def presetarse(self):
        return f"!Hola¡{self.sonido} es toy feliz de verte me llamo {self.nombre}" 

class gato(mascotas):
    pass

    def descripcion(self, raza):
        return f"Soy de raza {raza}"

    def saludo(self):
        return f"Soy {self.nombre} mi sonido es {self.sonido} pertenesco a la clase " 

class perro(mascotas):
    pass

    def descripcion(self, raza):
        return f"Soy de raza {raza}"

    def saludo(self):
        return f"Soy {self.nombre} mi sonido es {self.sonido} pertenesco a la clase "   


gato1 = gato("Nieves","miau")
print(gato1.presetarse())
print(gato1.saludo())
print(gato1.descripcion("Burmés"))
print("<------------------------------------->")
perro1 = perro("Steven","woooof")
print(perro1.presetarse())
print(perro1.saludo())
print(perro1.descripcion("Bulldog"))
