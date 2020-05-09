import tkinter as tk
from service.TextModeService import TextModeService
from visualization.GameStats import GameStats


class TextMode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.display_text = tk.Text(self)
        self.service = TextModeService(self.display_text)
        self.configure(bg="#f9f8fd")

        self.title_photo = tk.PhotoImage(file=r"img/title_text_mode.png")
        self.time_photo = tk.PhotoImage(file=r"img/time.png")
        self.correct_photo = tk.PhotoImage(file=r"img/words_correct.png")
        self.incorrect_photo = tk.PhotoImage(file=r"img/words_incorrect.png")
        self.menu_photo = tk.PhotoImage(file=r"img/menu.png")
        self.play_stop_photo = tk.PhotoImage(file=r"img/play_stop.png")

        tk.Label(self, bg="#f9f8fd", image=self.title_photo, borderwidth=0). \
            pack()

        self.time_display = tk.Label(self, bg="#f9f8fd", image=self.time_photo, borderwidth=0) \
            .pack()
        self.time_label = tk.Label(self, bg="#f9f8fd", borderwidth=0,
                                   text="%ds" % self.service.time, font=("Helvetica", 16))
        self.time_label.pack()

        self.display_text.tag_configure("center", justify='center')

        self.display_text.tag_configure("good", foreground="blue")
        self.display_text.tag_configure("bad", foreground="red")
        self.display_text.tag_configure("next", background="gray")
        self.display_text.pack()

        tk.Button(self, image=self.play_stop_photo, bg="#f9f8fd", borderwidth=0,
                  command=self.start_stop_game).pack(pady=(5, 20))

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
        self.controller.bind("<Key>", self.on_key_click)

    def stop_game(self):
        self.controller.unbind("<Key>")
        self.reset_labels()
        self.service.stop_game()
        frame = GameStats(self.parent, self.controller, self.service, "TextMode")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def on_key_click(self, event):
        if not self.service.start_typing:
            self.service.start_typing = True

        if event.char == '' or event.char == '\r':
            return

        # Action on backsapce
        if event.char == '\x08':
            self.service.action_on_backspace()
            return

        # End of word action
        if self.service.text[self.service.line_index][self.service.letter_line_index] == " ":
            if event.char != ' ':
                return
            self.service.end_of_word()

        # End of line action
        if self.service.text[self.service.line_index][self.service.letter_line_index + 1] == '\n':
            self.service.end_of_line()
            return

        self.service.word_change_action(event.char)

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
        self.time_label.configure(text="%ds" % self.service.game_time)
        self.display_text.configure(state="normal")
        self.display_text.delete('1.0', "end")
        self.display_text.configure(state="disabled")
