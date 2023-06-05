import pickle
from Vehiculo import Vehiculo

Moto = Vehiculo("Moto", 2, 0)
Coche = Vehiculo("Coche", 4, 5)
Camion = Vehiculo("Camión", 6, 3)

motos = open("motos.bin", "wb")
pickle.dump(Moto, motos)
motos.close()

coches = open("coches.bin","wb")
pickle.dump(Coche, coches)
coches.close()

camiones = open("camiones.bin","wb")
pickle.dump(Camion, camiones)
camiones.close()

motos = open("motos.bin","rb")
Moto = pickle.load(motos)
print(Moto.get_puertas())
motos.close()

coches = open("coches.bin","rb")
Coche = pickle.load(coches)
print(Coche.get_puertas())
coches.close()
