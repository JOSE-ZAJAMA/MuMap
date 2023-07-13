class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def __str__(self):
        return f"Ruta: {self.nombre}"

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destinos": self.destinos
        }

    @classmethod
    def from_json(cls, data):
        return cls(data["id"], data["nombre"], data["destinos"])
