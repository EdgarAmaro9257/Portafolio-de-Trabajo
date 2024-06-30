from datetime import date

class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.total = self.calcular_total()

    def calcular_total(self):
        dias = (self.fecha_fin - self.fecha_inicio).days
        return dias * self.habitacion.precio_por_noche

    def __str__(self):
        return (f"Reserva:\nCliente: {self.cliente}\nHabitación: {self.habitacion.numero}\n"
                f"Fecha inicio: {self.fecha_inicio}\nFecha fin: {self.fecha_fin}\n"
                f"Total: {self.total}")
