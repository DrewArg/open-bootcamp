'''
En este segundo ejercicio, tendréis que crear un programa que tenga
una clase llamada Alumno que tenga como atributos su nombre y su nota.
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y
mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''


class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print('El alumno', self.nombre, 'tiene una nota de', self.nota)

    def aprobado(self):
        print(False if self.nota < 7 else True)

a = Alumno("Andres",8)
e = Alumno("Ezequiel",4)

a.mostrar_datos()
a.aprobado()

e.mostrar_datos()
e.aprobado()