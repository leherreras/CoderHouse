class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def hablar(self):
        print(f"El tipo de animal {type(self).__name__} no puede hablar")

    def moverse(self):
        raise(NotImplementedError)

    def describeme(self):
        print(f"Soy un animal de tipo {type(self).__name__}")


class Perro(Animal):
    def __init__(self, especie, edad, duenio) -> None:
        super().__init__(especie, edad)
        self.duenio = duenio

    def hablar(self):
        print("Waff")
    
    def moverse(self):
        print("Camina con 4 patas")
    
    @staticmethod
    def morder():
        print("Ten cuidado que los perros muerden")

mi_perro = Perro('mamifero', 10)
mi_perro.hablar()
mi_perro.moverse()
mi_perro.describeme()
Perro.morder()