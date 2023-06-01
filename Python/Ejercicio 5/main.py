'''
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
'''

divisible_por_cuatro = lambda anio: True if anio % 4 == 0 else False
divisible_por_cuatrocientos = lambda anio: True if anio % 400 == 0 else False

anio = int(input())

if divisible_por_cuatro(anio) and divisible_por_cuatrocientos(anio):
    print("El año",anio,"es bisiesto")
else:
    print("Eñ año",anio,"no es bisiesto")
