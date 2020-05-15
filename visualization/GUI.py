import tkinter as tk
from tkinter import font

from visualization.GameStats import GameStats
from visualization.MainMenu import MainMenu
from visualization.GlobalStats import GlobalStats
from visualization.OneWordMode import OneWordMode
from visualization.TextMode import TextMode


# Przechowuje wszystkie strony aplikacji oraz odpowiada za przelaczanie ich
class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Become Typing Machine!")
        self.geometry("1000x720")
        self.title_font = font.Font(family="Helvetica", size=20)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=5)
        self.container.grid_columnconfigure(0, weight=5)

        self.frames = {}

        for page in (MainMenu, GlobalStats, OneWordMode, TextMode):
            page_name = page.__name__
            frame = page(self.container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainMenu")

    # Odpowiada za przelaczanie stron
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_stats(self, service):
        frame = GameStats(self.container, self, service)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
