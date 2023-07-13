import tkinter as tk
from tkinter import ttk
import json
import tkinter_mapview as mapview
from customstyle import CustomStyle
from usuarios import Usuario

class MuMap(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("MuMap")
        self.geometry("800x600")
        
        eventos_btn = ttk.Button(self, text="Índice de Eventos")
        eventos_btn.pack()

        busqueda_btn = ttk.Button(self, text="Búsqueda y Filtrado de Eventos")
        busqueda_btn.pack()

        historial_btn = ttk.Button(self, text="Historial de Eventos")
        historial_btn.pack()

        self.cargar_eventos()

    def cargar_eventos(self):
        try:
            with open("data/eventos.json", "r") as file:
                eventos_data = json.load(file)
                self.eventos = [Evento.from_json(evento) for evento in eventos_data]
        except FileNotFoundError:
            self.eventos = []

        # Aquí puedes hacer algo con los eventos cargados, como mostrarlos en la interfaz de usuario
        self.mostrar_indice_eventos()

    def guardar_eventos(self, eventos):
        eventos_data = [evento.to_json() for evento in eventos]
        with open("data/eventos.json", "w") as file:
            json.dump(eventos_data, file, indent=4)

    def mostrar_indice_eventos(self):
        for evento in self.eventos:
            evento_label = ttk.Label(self, text=evento.nombre, cursor="hand2")
            evento_label.pack()

            # Al hacer clic en el evento, mostrar detalles completos
            evento_label.bind("<Button-1>", lambda event, e=evento: self.mostrar_detalles_evento(e))

    def mostrar_detalles_evento(self, evento):
        details_window = tk.Toplevel(self)
        details_window.title("Detalles del Evento")
        details_window.geometry("400x300")

        # Mostrar detalles completos del evento, como artista, género, ubicación, etc.
        evento_label = ttk.Label(details_window, text=f"Artista: {evento.artista}")
        evento_label.pack()

        # Agrega más etiquetas para otros detalles del evento

        # Mostrar imagen del evento
        imagen_url = evento.imagen
        imagen_label = ttk.Label(details_window)
        imagen_label.pack()

        # Carga y muestra la imagen utilizando tkinter.PhotoImage o bibliotecas como Pillow

    def mostrar_busqueda_eventos(self):
        # Aquí puedes implementar la funcionalidad de búsqueda y filtrado de eventos
        # Ejemplo:
        search_window = tk.Toplevel(self)
        search_window.title("Búsqueda y Filtrado de Eventos")
        search_window.geometry("400x300")

        # Agrega los widgets necesarios para la búsqueda y filtrado de eventos en search_window

        # Lógica para filtrar los eventos según los criterios seleccionados por el usuario
        eventos_filtrados = self.filtrar_eventos()

        # Mostrar los eventos filtrados en la interfaz de usuario

    def filtrar_eventos(self):
        # Lógica para filtrar los eventos según los criterios seleccionados por el usuario
        # Puedes utilizar métodos como filter(), list comprehension, etc.
        eventos_filtrados = []  # Inicializar la lista de eventos filtrados

        # Aquí debes implementar tu lógica de filtrado, por ejemplo:
        for evento in self.eventos:
            if evento.genero == "Rock":
                eventos_filtrados.append(evento)

        return eventos_filtrados

    def ordenar_eventos(self):
        # Lógica para ordenar los eventos según el criterio seleccionado por el usuario
        # Puedes utilizar el método sort() o sorted() con una función de comparación personalizada
        eventos_ordenados = sorted(self.eventos, key=lambda e: e.nombre)
        return eventos_ordenados

    def mostrar_historial_eventos(self):
        # Aquí puedes mostrar el historial de eventos del usuario en la interfaz de usuario

        # Ejemplo:
        history_window = tk.Toplevel(self)
        history_window.title("Historial de Eventos")
        history_window.geometry("400x300")

        # Agrega los widgets necesarios para mostrar el historial de eventos en history_window


if __name__ == "__main__":
    usuario = Usuario(1, "John", "Doe")
    print(usuario)
    app = MuMap()
    app.mainloop()
