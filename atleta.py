class Atleta:
    def __init__(self,nombre, apellido, altura, peso, telefono) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
        self.telefono = telefono
        self.imc = self.__imc()
    
    def __imc(self) -> float:
        return self.peso / (self.altura * self.altura)
    
    def get_imc(self):
        return self.imc

    def estado_obesidad(self):
        
        if self.imc < 18.5:
            print(f"{self.nombre} tiene peso: Inferior")
        elif self.imc < 24.9:
            print(f"{self.nombre} tiene: Normal")
