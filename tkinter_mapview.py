import tkinter as tk
import tkinter_mapview as mapview

class MapApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Map App")
        self.geometry("800x600")
        
        # Crea un widget de mapa
        self.map = mapview.MapView(self)
        self.map.pack(fill=tk.BOTH, expand=True)

        # Establece las coordenadas y el nivel de zoom inicial
        self.map.set_center(40.7128, -74.0060)  # Ejemplo: Nueva York
        self.map.set_zoom(10)  # Ejemplo: nivel de zoom 10

if __name__ == "__main__":
    app = MapApp()
    app.mainloop()