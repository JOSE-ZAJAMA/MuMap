class Artista:
    def __init__(self, id, nombre, genero, imagen):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.imagen = imagen

    def __str__(self):
        return f"{self.nombre}"

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "imagen": self.imagen
        }

    @classmethod
    def from_json(cls, data):
        return cls(data["id"], data["nombre"], data["genero"], data["imagen"])
