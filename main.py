import tkinter as tk
import customtkinter
import json

# CustomTkinter colores

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Dimensiones de la app

app = customtkinter.CTk()
app.geometry("720x480")

eventos_widgets = []  # Widgets para los eventos actuales

def mostrar_indice_eventos():
    # Widgets para mostrar los eventos en formato JSON
    # Eliminar los widgets de eventos anteriores
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

        estadio_label = tk.Label(evento_frame, text=f"Lugar: {evento['estadio']}")
        estadio_label.pack()

        artista_label = tk.Label(evento_frame, text=f"Artista: {evento['artista']}")
        artista_label.pack()

        genero_label = tk.Label(evento_frame, text=f"Género: {evento['genero']}")
        genero_label.pack()

        ubicacion_label = tk.Label(evento_frame, text=f"Ubicación: {evento['ubicacion']}")
        ubicacion_label.pack()

        fecha_label = tk.Label(evento_frame, text=f"Fecha de evento: {evento['fecha']}")
        fecha_label.pack()
        
        horaInicio_label = tk.Label(evento_frame, text=f"Hora de inicio del evento: {evento['horaInicio']}")
        horaInicio_label.pack()

        horaFin_label = tk.Label(evento_frame, text=f"Hora de cierre del evento: {evento['horaFin']}")
        horaFin_label.pack()

        descripcion_label = tk.Label(evento_frame, text=f"Descripción del evento: {evento['descripcion']}")
        descripcion_label.pack()

        cerrar_button = customtkinter.CTkButton(evento_frame, text="Cerrar ventana", command=evento_frame.destroy)
        cerrar_button.pack()

        # Almacena el frame del evento en la lista de widgets
        eventos_widgets.append(evento_frame)

def button_function(section):
    if section == "indice_eventos":
        mostrar_indice_eventos()

def mostrar_busqueda_eventos():
    # Lugar para los nuevos widgets para realizar la búsqueda y mostrar los resultados
    pass

def mostrar_historial_eventos():
    # Lugar para crear nuevos widgets para mostrar el historial en formato JSON
    pass

def button_function(section):
    if section == "indice_eventos":
        mostrar_indice_eventos()
    elif section == "busqueda_eventos":
        mostrar_busqueda_eventos()
    elif section == "historial_eventos":
        mostrar_historial_eventos()

welcome_label = customtkinter.CTkLabel(master=app, text="Bienvenido a NOMBRE DE LA APP", font=("Roboto", 24))
welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button1 = customtkinter.CTkButton(master=app, text="Índice de Eventos", command=lambda: button_function("indice_eventos"))
button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Búsqueda y Filtrado de Eventos", command=lambda: button_function("busqueda_eventos"))
button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button3 = customtkinter.CTkButton(master=app, text="Historial de Eventos", command=lambda: button_function("historial_eventos"))
button3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

app.title("TITULO DE LA APP")
app.mainloop()
