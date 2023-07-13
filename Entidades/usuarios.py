"""Usuario
id (int): El identificador único del usuario.
nombre (str): El nombre del usuario.
apellido (str): El apellido del usuario.
historial_eventos (List[int]): Una lista de IDs de 
eventos a los que ha asistido el usuario."""
class Usuario:
    def __init__(self,id,nombre,apellido,historial_eventos = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial_eventos is None:
            self.historial_eventos = []
        else:
            self.historial_eventos = historial_eventos
    
    def __str__(self):
        return f"{self.nombre}"
    
    def to_json(self):
        return {
            "id":self.id,
            "apellido" : self.apellido
        }
        
    @classmethod
    def from_json(self,data):
        return "objeto usuario"