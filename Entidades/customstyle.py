import tkinter.ttk as ttk

class CustomStyle:
    def __init__(self):
        self.bg_color = "lightgray"
        self.fg_color = "black"
        self.font = ("Arial", 12, "bold")
        self.button_bg = "blue"
        self.button_fg = "white"
        self.button_font = ("Arial", 10, "bold")

    def apply_styles(self):
        ttk.Style().configure("Custom.TLabel", background=self.bg_color, foreground=self.fg_color, font=self.font)
        ttk.Style().configure("Custom.TButton", background=self.button_bg, foreground=self.button_fg, font=self.button_font)
