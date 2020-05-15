import tkinter as tk
import service.HttpModule

from service.GameService import GameService


class GameStats(tk.Frame):
    def __init__(self, parent, controller, service, prev):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.save_window = None
        self.prev = prev

        self.stat_time = service.game_time - service.time
        if self.stat_time == 0:
            self.stat_wpm = 0
            self.stat_cpm = 0
        else:
            self.stat_wpm = (service.words_correct + service.words_incorrect) / (self.stat_time / 60)
            self.stat_cpm = service.char_counter / (self.stat_time / 60)

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
        tk.Label(self, text="{:.2f}".format(self.stat_wpm), font=("Helvetica", 16), bg="#f9f8fd") \
            .grid(row=2, column=1, pady=(0, 20))

        tk.Label(self, image=self.cpm, bg="#f9f8fd").grid(row=3, column=1)
        tk.Label(self, text="{:.2f}".format(self.stat_cpm), font=("Helvetica", 16), bg="#f9f8fd") \
            .grid(row=4, column=1, pady=(0, 20))

        tk.Label(self, image=self.time, bg="#f9f8fd").grid(row=5, column=1)
        tk.Label(self, text="{}s".format(self.stat_time), font=("Helvetica", 16), bg="#f9f8fd") \
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
        self.save_window = tk.Toplevel()
        self.save_window.wm_title("Become a typing machine!")
        self.save_window.config(bg="#f9f8fd")
        tk.Label(self.save_window, image=self.insert_name, bg="#f9f8fd").pack()
        entry = tk.Entry(self.save_window, bg="#f9f8fd", bd=1, font=("Comic Sans MS", 20), justify='center')
        entry.pack(pady=(10, 10))

        tk.Button(self.save_window, image=self.save2, bd=0,
                  command=lambda: self.save_f(entry.get())).pack(pady=(5, 0))

    def save_f(self, name):
        if name:
            service.HttpModule.save_result(name, self.prev, self.stat_cpm, self.stat_wpm, self.stat_time)
        self.save_window.destroy()




