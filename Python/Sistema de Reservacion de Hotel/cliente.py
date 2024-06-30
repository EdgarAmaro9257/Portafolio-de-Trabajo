class Cliente:
    def __init__(self, nombre, documento_identidad):
        self.nombre = nombre
        self.documento_identidad = documento_identidad

    def __str__(self):
        return f"Cliente: {self.nombre}, Documento: {self.documento_identidad}"
