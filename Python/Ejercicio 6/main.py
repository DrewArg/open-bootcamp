'''
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
Color
Ruedas
Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
'''

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    color = None
    ruedas = None
    puertas = None

    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    @abstractmethod
    def encender(self):
        pass

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self,color, ruedas, puertas, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super(Coche, self).__init__(color,ruedas,puertas)

    def encender(self):
        print("encendido")

c = Coche("rojo",4,3,150,1500)

c.encender()
print(c.color,c.ruedas,c.velocidad,c.cilindrada,c.puertas)