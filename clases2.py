class Persona:
    #Atributos
    especie= 'humano'
    extremidades = 4

    #constructor
    def __init__(self,nombre: str,edad):
        print(f'Creando persona: {nombre}, {edad} años')
    
    #Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    
    #metodos
    @staticmethod
    def correr(velocidad):
        print(f'Está corriendo a {velocidad} km/h')
    
    @staticmethod
    def saluda():
        print("Hola!")

persona1= Persona("Juan","25")
print(Persona.extremidades)
Persona.saluda()
Persona.correr(10)
