import getpass
import sqlite3

# CREATE TABLE alumnos(nombre TEXT NOT NULL, apellido TEXT NOT NULL);
def main():
    alumnos = {
        0: ["jose","botellas"],
        1: ["raul","perez"],
        2: ["maria","fernandez"],
        3: ["carlota","nieves"],
        4: ["juan","gonzales"],
        5: ["fernanda","gonzalez"],
        6: ["laura","triton"],
        7: ["ezequiel","rodriguez"]
    }

    for key in alumnos.keys():
       crear_alumno(alumnos[key][0],alumnos[key][1])

    print(ver_alumnos())

    buscar_nombre = input("nombre: ")
    buscar_apellido = input("apellido: ")

    alumno = buscar_alumno(buscar_nombre,buscar_apellido)

    print(alumno)

def crear_alumno(nombre, apellido):
    connection = sqlite3.connect("ejercicio16.db")
    cursor = connection.cursor()

    query = '''INSERT INTO alumnos(nombre, apellido)VALUES(?,?)'''

    cursor.execute(query,(nombre, apellido))

    connection.commit()
    cursor.close()
    connection.close()

def ver_alumnos():
    connection = sqlite3.connect("ejercicio16.db")
    cursor = connection.cursor()

    query = '''SELECT rowid, nombre, apellido from alumnos;'''

    rows = cursor.execute(query)
    data = rows.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return data

def buscar_alumno(nombre, apellido):
    connection = sqlite3.connect("ejercicio16.db")
    cursor = connection.cursor()

    query = f'SELECT rowid, nombre, apellido FROM alumnos WHERE nombre="{nombre}" AND apellido="{apellido}";'

    rows = cursor.execute(query)
    data = rows.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    return data

if __name__ == '__main__':
    main()
