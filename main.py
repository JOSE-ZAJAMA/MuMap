import tkinter as tk
import customtkinter
import json

#Colores personalizados
purple_dark = "#2F242C"
gray_light = "#E5E5E5"
yellow = "#E6D884"
green_light = "#A1A892"

eventos_widgets = []  # Widgets para los eventos actuales

# Función mostrar_indice_eventos
def mostrar_indice_eventos():
    for widget in eventos_widgets:
        widget.destroy()
    
    try:
        with open("data/eventos.json", "r") as file:
            eventos_data = json.load(file)
    except FileNotFoundError:
        eventos_data = []

    for evento in eventos_data:
        evento_frame = tk.Frame(app)
        evento_frame.pack()

        estadio_frame = tk.Frame(evento_frame)
        estadio_frame.pack()

        estadio_label = tk.Label(estadio_frame, text=f"Lugar: {evento['estadio']}")
        estadio_label.pack()

        artista_label = tk.Label(evento_frame, text=f"Artista: {evento['artista']}")
        artista_label.pack()

        ver_button = tk.Button(evento_frame, text="Ver Detalles", command=lambda id=evento['id']: mostrar_detalle_evento(id))
        ver_button.pack()

        eventos_widgets.append(evento_frame)

def mostrar_detalle_evento(evento_id):
    detalle_frame = tk.Toplevel(app)
    detalle_frame.title("Detalles del Evento")
    detalle_frame.geometry("400x300")

    try:
        with open("data/eventos.json", "r") as file:
            eventos_data = json.load(file)
            evento = next((evento for evento in eventos_data if evento['id'] == evento_id), None)
    except FileNotFoundError:
        evento = None

    if evento:
        estadio_label = tk.Label(detalle_frame, text=f"Nombre: {evento['estadio']}")
        estadio_label.pack()

        artista_label = tk.Label(detalle_frame, text=f"Artista: {evento['artista']}")
        artista_label.pack()

        genero_label = tk.Label(detalle_frame, text=f"Género: {evento['genero']}")
        genero_label.pack()

        descripcion_label = tk.Label(detalle_frame, text=f"Descripción: {evento['descripcion']}")
        descripcion_label.pack()

        cerrar_button = tk.Button(detalle_frame, text="Cerrar ventana", command=detalle_frame.destroy)
        cerrar_button.pack()
    else:
        mensaje_label = tk.Label(detalle_frame, text="No se encontró información del evento.")
        mensaje_label.pack()

def button_function(section):
    if section == "indice_eventos":
        mostrar_indice_eventos()

# Dimensiones de la ventana principal de la aplicación
app = tk.Tk()
app.geometry("720x480")
app.title("♫ TITULO DE LA APP ♫")

# Widgets para la interfaz de usuario
welcome_label = tk.Label(app, text="Bienvenido a NOMBRE DE LA APP", font=("Arial", 24), fg=purple_dark)
welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button1 = tk.Button(app, text="Índice de Eventos", command=lambda: button_function("indice_eventos"), bg=yellow, fg=purple_dark)
button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button2 = tk.Button(app, text="Búsqueda y Filtrado de Eventos", command=lambda: button_function("busqueda_eventos"), bg=yellow, fg=purple_dark)
button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button3 = tk.Button(app, text="Historial de Eventos", command=lambda: button_function("historial_eventos"), bg=yellow, fg=purple_dark)
button3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Inicia el bucle principal de la aplicación
app.mainloop()
