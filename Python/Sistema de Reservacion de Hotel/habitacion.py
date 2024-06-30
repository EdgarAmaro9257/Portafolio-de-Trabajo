class Habitacion:
    def __init__(self, numero, tipo, precio_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche
        self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}) - {estado} - Precio: {self.precio_por_noche} por noche"
