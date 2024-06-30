from habitacion import Habitacion
from reserva import Reserva

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def listar_habitaciones_disponibles(self):
        return [habitacion for habitacion in self.habitaciones if not habitacion.ocupada]

    def hacer_reserva(self, cliente, numero_habitacion, fecha_inicio, fecha_fin):
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion), None)
        if habitacion and not habitacion.ocupada:
            reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
            self.reservas.append(reserva)
            habitacion.ocupada = True
            return reserva
        else:
            return None

    def __str__(self):
        return f"Hotel {self.nombre} - Habitaciones: {len(self.habitaciones)}, Reservas: {len(self.reservas)}"
