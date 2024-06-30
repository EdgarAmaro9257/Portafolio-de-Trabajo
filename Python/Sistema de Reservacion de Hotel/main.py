from datetime import date
from cliente import Cliente
from habitacion import Habitacion
from hotel import Hotel

def obtener_fecha(mensaje):
    while True:
        fecha_str = input(mensaje + " (YYYY-MM-DD): ")
        try:
            return date.fromisoformat(fecha_str)
        except ValueError:
            print("Formato de fecha inválido. Intenta nuevamente.")

def main():
    # Crear hotel
    hotel = Hotel("Hotel Python")

    # Crear y agregar habitaciones al hotel
    hotel.agregar_habitacion(Habitacion(101, "Individual", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 150))

    # Crear cliente a partir de la entrada del usuario
    nombre_cliente = input("Ingrese su nombre completo: ")
    documento_identidad = input("Ingrese su documento de identidad: ")
    cliente = Cliente(nombre_cliente, documento_identidad)

    # Listar habitaciones disponibles
    print("Habitaciones disponibles:")
    habitaciones_disponibles = hotel.listar_habitaciones_disponibles()
    for habitacion in habitaciones_disponibles:
        print(habitacion)

    # Solicitar la habitación deseada
    numero_habitacion = int(input("Ingrese el número de la habitación que desea reservar: "))

    # Solicitar fechas de reserva
    fecha_inicio = obtener_fecha("Ingrese la fecha de inicio de la reserva")
    fecha_fin = obtener_fecha("Ingrese la fecha de fin de la reserva")

    # Hacer una reserva
    reserva = hotel.hacer_reserva(cliente, numero_habitacion, fecha_inicio, fecha_fin)
    if reserva:
        print("Reserva realizada con éxito:")
        print(reserva)
    else:
        print("No se pudo realizar la reserva. La habitación no está disponible.")

    # Listar habitaciones disponibles después de la reserva
    print("Habitaciones disponibles después de la reserva:")
    habitaciones_disponibles = hotel.listar_habitaciones_disponibles()
    for habitacion in habitaciones_disponibles:
        print(habitacion)

if __name__ == "__main__":
    main()
