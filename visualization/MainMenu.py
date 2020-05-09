import tkinter as tk
from PIL import ImageTk, Image


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text="Main Menu", font=controller.title_font, bg="#f9f8fd")
        # label.pack(fill="x", pady=10)
        self.configure(bg="#f9f8fd")

        self.title = tk.PhotoImage(file=r"img/title.png")
        self.word = tk.PhotoImage(file=r"img/wordmode.png")
        self.text = tk.PhotoImage(file=r"img/textmode.png")
        self.stats = tk.PhotoImage(file=r"img/statistics.png")
        self.machine = tk.PhotoImage(file=r"img/machine.png")
        self.exit = tk.PhotoImage(file=r"img/exit.png")

        tk.Label(self, image=self.title, bg="#f9f8fd").grid(row=0, column=0, columnspan=2)

        word_mode_button = tk.Button(self, bg="#f9f8fd", image=self.word, borderwidth=0,
                                     command=lambda: controller.show_frame("OneWordMode"))
        word_mode_button.grid(row=1, column=0, pady="30")

        text_mode_button = tk.Button(self, bg="#f9f8fd", image=self.text, borderwidth=0,
                                     command=lambda: controller.show_frame("TextMode"))
        text_mode_button.grid(row=2, column=0, pady="30")

        global_stats_button = tk.Button(self, bg="#f9f8fd", image=self.stats, borderwidth=0,
                                        command=lambda: controller.show_frame("GlobalStats"))
        global_stats_button.grid(row=3, column=0, pady="30")

        exit_button = tk.Button(self, bg="#f9f8fd", image=self.exit, borderwidth=0,
                                command=lambda: exit(0))
        exit_button.grid(row=4, column=0, pady="30")

        tk.Label(self, image=self.machine, bg="#f9f8fd").grid(row=1, column=1, rowspan=4)
