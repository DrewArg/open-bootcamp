

class Vehiculo:
    ruedas = None
    puertas = None

    def __init__(self,nombre, ruedas, puertas):
        self.nombre = nombre
        self.ruedas = ruedas
        self.puertas = puertas

    def get_nombre(self):
        return self.nombre

    def get_ruedas(self):
        return self.ruedas

    def get_puertas(self):
        return self.puertas


