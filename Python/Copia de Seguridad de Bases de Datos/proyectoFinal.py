########################################## 
########################################## 
# PROYECTO FINAL DE PYTHON INTERMEDIO AM # 
##########################################
##########################################

#Nombre: Edgar Amaro Cantoral
#Crear un script que haga un CRUD de una base de datos y archivos para
#crear una copia de seguridad (backup) de una base de datos SQLite.
import sqlite3
import shutil
import os

def crear_tabla():
    conexion = sqlite3.connect('baseDeDatos.db')
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        apellidoPaterno TEXT NOT NULL,
                        apellidoMaterno TEXT NOT NULL,
                        curp INTEGER NOT NULL,
                        edad INTEGER NOT NULL)''')

    conexion.commit()
    conexion.close()

def validar_curp(curp):
    if len(curp) == 18:
        return True
    else:
        return False

def validar_edad(edad):
    if len(str(edad)) <= 3:
        return True
    else:
        return False


def insertar_datos(nombre, apellidoPaterno, apellidoMaterno, curp, edad):
    while not validar_curp(curp) or len(curp) != 18:
        print("Error: El CURP debe tener exactamente 18 caracteres.")
        curp = input("Ingresa el CURP (18 caracteres): ")

    while not validar_edad(edad) or len(str(edad)) != 3:
        print("Error: La edad debe tener exactamente 3 dígitos.")
        try:
            edad = int(input("Ingresa la edad (3 dígitos): "))
        except ValueError:
            print("Error: Ingresa un valor numérico para la edad.")
            edad = 0

    conexion = sqlite3.connect('baseDeDatos.db')
    cursor = conexion.cursor()

    cursor.execute('''INSERT INTO datos (nombre, apellidoPaterno, apellidoMaterno, curp, edad) VALUES (?, ?, ?, ?, ?)''', (nombre, apellidoPaterno, apellidoMaterno, curp, edad))

    conexion.commit()
    conexion.close()

def mostrar_datos():
    conexion = sqlite3.connect('baseDeDatos.db')
    cursor = conexion.cursor()

    cursor.execute('''SELECT * FROM datos''')
    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

    conexion.close()

def actualizar_datos(id):
    conexion = sqlite3.connect('baseDeDatos.db')
    cursor = conexion.cursor()

    print("Selecciona el campo que deseas modificar:")
    print("1. Nombre")
    print("2. Apellido Paterno")
    print("3. Apellido Materno")
    print("4. CURP")
    print("5. Edad")
    campo = int(input("Ingresa el número del campo a modificar: "))

    if campo == 1:
        nombre = input("Ingresa el nuevo nombre: ")
        cursor.execute('''UPDATE datos SET nombre=? WHERE id=?''', (nombre, id))

    elif campo == 2:
        apellidoPaterno = input("Ingresa el nuevo apellido paterno: ")
        cursor.execute('''UPDATE datos SET apellidoPaterno=? WHERE id=?''', (apellidoPaterno, id))

    elif campo == 3:
        apellidoMaterno = input("Ingresa el nuevo apellido materno: ")
        cursor.execute('''UPDATE datos SET apellidoMaterno=? WHERE id=?''', (apellidoMaterno, id))

    elif campo == 4:
        curp = input("Ingresa el nuevo CURP: ")
        cursor.execute('''UPDATE datos SET curp=? WHERE id=?''', (curp, id))

    elif campo == 5:
        edad = int(input("Ingresa la nueva edad: "))
        cursor.execute('''UPDATE datos SET edad=? WHERE id=?''', (edad, id))

    else:
        print("Opción inválida. No se realizarán cambios.")

    conexion.commit()
    conexion.close()

def borrar_datos(id):
    conexion = sqlite3.connect('baseDeDatos.db')
    cursor = conexion.cursor()

    cursor.execute('''DELETE FROM datos WHERE id=?''', (id,))

    conexion.commit()
    conexion.close()

def hacer_backup():
    if os.path.exists('baseDeDatos.db'):
        shutil.copyfile('baseDeDatos.db', 'backup_baseDeDatos.db')
        print("Copia de seguridad creada con éxito.")
    else:
        print("La base de datos no existe. Primero crea la base de datos y luego realiza una copia de seguridad.")

if __name__ == "__main__":
    crear_tabla()

    while True:
        print("\n1. Insertar datos")
        print("2. Mostrar datos")
        print("3. Actualizar datos")
        print("4. Borrar datos")
        print("5. Hacer backup")
        print("6. Salir")

        opcion = int(input("Presiona un numero para ingresar a la opción deseada: "))

        if opcion == 1:
            nombre = input("Ingresa el nombre: ")
            apellidoPaterno = input("Ingresa el apellido paterno: ")
            apellidoMaterno = input("Ingresa el apellido materno: ")
            curp= input("Ingresa el CURP: ")
            edad = int(input("Ingresa la edad: "))
            insertar_datos(nombre, apellidoPaterno, apellidoMaterno, curp, edad)

        elif opcion == 2:
            mostrar_datos()

        elif opcion == 3:
            id = int(input("Ingresa el ID del registro a actualizar: "))
            actualizar_datos(id)

        elif opcion == 4:
            id = int(input("Ingresa el ID del registro a borrar: "))
            borrar_datos(id)

        elif opcion == 5:
            hacer_backup()

        elif opcion == 6:
            break

        else:
            print("Opción inválida. Por favor, ingresa una opción válida.")

