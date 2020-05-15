import tkinter as tk

from service.GameService import GameService


class GameStats(tk.Frame):
    def __init__(self, parent, controller, service, prev):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        stat_time = service.game_time - service.time
        if stat_time == 0:
            stat_wpm = 0
            stat_cpm = 0
        else:
            stat_wpm = (service.words_correct + service.words_incorrect) / (stat_time / 60)
            stat_cpm = service.char_counter / (stat_time / 60)

        self.configure(bg="#f9f8fd")

        self.title = tk.PhotoImage(file=r"img/youdidit.png")
        self.wpm = tk.PhotoImage(file=r"img/wpm.png")
        self.cpm = tk.PhotoImage(file=r"img/cpm.png")
        self.time = tk.PhotoImage(file=r"img/time.png")
        self.errors = tk.PhotoImage(file=r"img/errors.png")
        self.back = tk.PhotoImage(file=r"img/back.png")
        self.menu = tk.PhotoImage(file=r"img/menu.png")
        self.save = tk.PhotoImage(file=r"img/save.png")
        self.insert_name = tk.PhotoImage(file=r"img/insert_name.png")
        self.save2 = tk.PhotoImage(file=r"img/save2.png")

        tk.Label(self, image=self.title, bg="#f9f8fd").grid(row=0, columnspan=3)

        tk.Label(self, image=self.wpm, bg="#f9f8fd").grid(row=1, column=1)
        tk.Label(self, text="{:.2f}".format(stat_wpm), font=("Helvetica", 16), bg="#f9f8fd") \
            .grid(row=2, column=1, pady=(0, 20))

        tk.Label(self, image=self.cpm, bg="#f9f8fd").grid(row=3, column=1)
        tk.Label(self, text="{:.2f}".format(stat_cpm), font=("Helvetica", 16), bg="#f9f8fd") \
            .grid(row=4, column=1, pady=(0, 20))

        tk.Label(self, image=self.time, bg="#f9f8fd").grid(row=5, column=1)
        tk.Label(self, text="{}s".format(stat_time), font=("Helvetica", 16), bg="#f9f8fd") \
            .grid(row=6, column=1, pady=(0, 20))

        tk.Label(self, image=self.errors, bg="#f9f8fd").grid(row=7, column=1)
        tk.Label(self, text="{}".format(service.words_incorrect),
                 font=("Helvetica", 16), bg="#f9f8fd").grid(row=8, column=1)

        tk.Button(self, image=self.back, bg="#f9f8fd", borderwidth=0,
                  command=lambda: controller.show_frame(prev)).grid(row=9, column=0)

        tk.Button(self, image=self.menu, bg="#f9f8fd", borderwidth=0,
                  command=lambda: controller.show_frame("MainMenu")).grid(row=9, column=2)

        tk.Button(self, image=self.save, bg="#f9f8fd", borderwidth=0,
                  command=self.popup).grid(row=9, column=1)

    def popup(self):
        win = tk.Toplevel()
        win.wm_title("Become a typing machine!")
        win.config(bg="#f9f8fd")
        tk.Label(win, image=self.insert_name, bg="#f9f8fd").pack()
        tk.Entry(win, bg="#f9f8fd", bd=1, font=("Comic Sans MS", 20), justify='center')\
            .pack(pady=(10, 10))
        tk.Button(win, image=self.save2, bd=0, command=win.destroy).pack(pady=(5, 0))


