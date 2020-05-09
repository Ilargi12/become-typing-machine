import tkinter as tk


class GlobalStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Global Stats", font=controller.title_font)
        label.pack(fill="x", pady=10)

        info = tk.Label(self, text="Tu beda statystyki")
        info.pack()

        come_back_button = tk.Button(self, text="Come Back", command=lambda: controller.show_frame("MainMenu"))
        come_back_button.pack()