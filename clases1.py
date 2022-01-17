class Coche:


    def __init__(self, color, marca, modelo, *args, **kargs) -> None:
        self.color = color
        self.marca = marca
        self.modelo = modelo

    
    def mostrar_atributos(self):
        print(f"El color del carro es: {self.color}\nla marca es: {self.marca}\nel modelo es: {self.modelo}")

    def estacionar(self):
        self.parar()
        print("Estacionando coche")

    @staticmethod
    def arrancar():
        print("Arrancar coche")
    
    def parar(self):
        print("Parar coche")

Coche.arrancar()
coche1 = Coche("verde","toyota", 1988)
coche1.mostrar_atributos()
coche1.estacionar()