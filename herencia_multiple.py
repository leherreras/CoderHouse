class Mamifero:
    def __init__(self, cantidad_mamas, esperanza_de_vida) -> None:
        self.cantidad_mamas = cantidad_mamas
        self.esperanza_de_vida = esperanza_de_vida
    def mamar(self):
        pass
    def nacer(self):
        raise(NotImplementedError)
class AnimalMarino:
    def __init__(self, tiene_branqueas: bool, especie: str) -> None:
        self.tiene_branqueas = tiene_branqueas
        self.especie = especie
    def nadar(self):
        raise(NotImplementedError)

class Cetaceo(Mamifero, AnimalMarino):
    def __init__(self, 
    cantidad_mamas, esperanza_de_vida, 
    tiene_branqueas, especie, 
    notas, vive_en, peso) -> None:
        Mamifero.__init__(self, cantidad_mamas, esperanza_de_vida)
        AnimalMarino.__init__(self, tiene_branqueas, especie)
        self.notas = notas
        self.vive_en =vive_en
        self.peso = peso
    def nadar(self) -> str:
        return "El animal esta nadando"
    def nacer(self) -> bool:
        if self.peso > 0.5:
            return False
        return True

cetaceo_1 = Cetaceo(1, 4, True, "Mamifero","Misticeos mas pequeños", "agua", 20.3)
print(cetaceo_1.nadar())