import tkinter as tk
import tkinter.ttk as ttk

# Definición de los estilos personalizados
class CustomStyle:
    def __init__(self):
        self.bg_color = "lightgray"
        self.fg_color = "black"
        self.font = ("Arial", 12, "bold")
        self.button_bg = "blue"
        self.button_fg = "white"
        self.button_font = ("Arial", 10, "bold")

# Aplicación de los estilos personalizados
def apply_styles(style):
    # Estilos para los componentes de Tkinter
    ttk.Style().configure("Custom.TLabel", background=style.bg_color, foreground=style.fg_color, font=style.font)
    ttk.Style().configure("Custom.TButton", background=style.button_bg, foreground=style.button_fg, font=style.button_font)

# Ejemplo de uso
class CustomApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Custom App")

        # Crear una instancia de los estilos personalizados
        self.custom_style = CustomStyle()

        # Aplicar los estilos personalizados
        apply_styles(self.custom_style)

        # Crear componentes utilizando los estilos personalizados
        label = ttk.Label(self, text="Etiqueta personalizada", style="Custom.TLabel")
        label.pack(pady=10)

        button = ttk.Button(self, text="Botón personalizado", style="Custom.TButton")
        button.pack(pady=10)

if __name__ == "__main__":
    app = CustomApp()
    app.mainloop()
