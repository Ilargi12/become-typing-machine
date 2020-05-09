import tkinter as tk

from service.OneWordModeService import OneWordModeService
from visualization.GameStats import GameStats


class OneWordMode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.service = OneWordModeService()
        self.configure(bg="#f9f8fd")

        self.title_photo = tk.PhotoImage(file=r"img/title_word_mode.png")
        self.word_to_type_photo = tk.PhotoImage(file=r"img/word_to_type.png")
        self.place_to_type_photo = tk.PhotoImage(file=r"img/place_to_type.png")
        self.time_photo = tk.PhotoImage(file=r"img/time.png")
        self.correct_photo = tk.PhotoImage(file=r"img/words_correct.png")
        self.incorrect_photo = tk.PhotoImage(file=r"img/words_incorrect.png")
        self.menu_photo = tk.PhotoImage(file=r"img/menu.png")
        self.play_stop_photo = tk.PhotoImage(file=r"img/play_stop.png")

        game_type_label = tk.Label(self, bg="#f9f8fd", image=self.title_photo, borderwidth=0).pack()

        display_label = tk.Label(self, bg="#f9f8fd", image=self.word_to_type_photo, borderwidth=0).pack(pady=(15, 0))
        self.entry = tk.Label(self, bg="#f9f8fd", bd=0, font=("Comic Sans MS", 20, "bold"))
        self.entry.pack()

        text_label = tk.Label(self, bg="#f9f8fd", image=self.place_to_type_photo, borderwidth=0).pack()
        self.text = tk.Entry(self, bg="#f9f8fd", bd=0, font=("Comic Sans MS", 20), justify='center',
                             disabledbackground="#f9f8fd", state="disabled")
        self.text.pack()

        self.time_display = tk.Label(self, bg="#f9f8fd", image=self.time_photo, borderwidth=0).pack()
        self.time_label = tk.Label(self, bg="#f9f8fd", borderwidth=0,
                                   text="%ds" % self.service.time, font=("Helvetica", 16))
        self.time_label.pack()

        self.correct_display = tk.Label(self, bg="#f9f8fd", image=self.correct_photo, borderwidth=0).pack()
        self.correct_label = tk.Label(self, bg="#f9f8fd", borderwidth=0,
                                      text="%d" % self.service.words_correct, font=("Helvetica", 16))
        self.correct_label.pack()

        self.incorrect_display = tk.Label(self, bg="#f9f8fd", image=self.incorrect_photo, borderwidth=0).pack()
        self.incorrect_label = tk.Label(self, bg="#f9f8fd", borderwidth=0,
                                        text="%d" % self.service.words_incorrect, font=("Helvetica", 16))
        self.incorrect_label.pack()

        tk.Button(self, image=self.play_stop_photo, bg="#f9f8fd", borderwidth=0,
                  command=self.start_stop_game).pack(pady=(30, 40))

        tk.Button(self, image=self.menu_photo, bg="#f9f8fd", borderwidth=0,
                  command=lambda: self.go_to_menu()).pack()

        self.refresh_time()

    def start_stop_game(self):
        if not self.service.game_active:
            self.start_game()
        else:
            self.stop_game()

    def start_game(self):
        self.service.start_game()
        self.text.configure(state="normal")
        self.controller.bind("<Return>", self.on_click)
        self.controller.bind("<space>", self.on_click)
        self.controller.bind("<Key>", self.on_key_click)
        self.display_word()

    def stop_game(self):
        self.controller.unbind("<Key>")
        self.controller.unbind("<Return>")
        self.controller.unbind("<space>")

        frame = GameStats(self.parent, self.controller, self.service, "OneWordMode")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

        self.service.stop_game()
        self.reset_labels()

    def on_click(self, event=None):
        self.service.check_word(self.text.get().strip())
        self.correct_label.configure(text="%d" % self.service.words_correct)
        self.incorrect_label.configure(text="%d" % self.service.words_incorrect)
        self.text.delete(0, 'end')
        self.display_word()

    def on_key_click(self, event=None):
        if not self.service.start_typing:
            self.service.start_typing = True

    def display_word(self):
        word = self.service.get_random_word()
        self.entry.configure(text=word)

    def refresh_time(self):
        if self.service.start_typing:
            if self.service.refresh_game():
                self.time_label.configure(text="%ds" % self.service.time)
            else:
                self.stop_game()
        self.after(1000, self.refresh_time)

    def go_to_menu(self):
        self.service.stop_game()
        self.reset_labels()
        self.controller.show_frame("MainMenu")

    def reset_labels(self):
        self.text.delete(0, tk.END)
        self.text.configure(state="disabled")
        self.entry.configure(text="")
        self.time_label.configure(text="%ds" % self.service.game_time)
        self.correct_label.configure(text="%d" % 0)
        self.incorrect_label.configure(text="%d" % 0)
