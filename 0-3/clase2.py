class Persona:
    nombre = " "

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return "hola mi nombre es " + self.apellido


