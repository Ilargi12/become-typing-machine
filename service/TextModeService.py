from service.GameService import GameService


class TextModeService(GameService):
    def __init__(self, display_text):
        GameService.__init__(self)
        self.letter_line_index = 0
        self.line_index = 0
        self.mistakes_index_list = []
        self.text = []
        self.display_text = display_text

    def start_game(self):
        super(TextModeService, self).start_game()
        self.letter_line_index = 1
        self.line_index = 0
        self.mistakes_index_list = []
        self.text = self.generator.get_random_sentences()
        self.display_text.configure(state="normal")
        self.display_text.delete('1.0', "end")
        for string in self.text:
            self.display_text.insert("end", string)
        self.display_text.tag_add("center", "1.0", "end")
        self.display_text.configure(state="disabled")
        self.display_text.tag_add("next", "1.1", "1.2")

    def end_of_word(self):
        if not self.mistakes_index_list:
            self.words_correct += 1
        else:
            self.words_incorrect += 1
            self.mistakes_index_list.clear()

    def action_on_backspace(self):
        if self.letter_line_index == 1 or self.text[self.line_index][self.letter_line_index - 1] == " ":
            return

        self.display_text.tag_remove("next", f"{self.line_index + 1}.{self.letter_line_index}",
                                     f"{self.line_index + 1}.{self.letter_line_index + 1}")

        self.letter_line_index -= 1
        if f"{self.line_index + 1}.{self.letter_line_index}" in self.mistakes_index_list:
            self.mistakes_index_list.remove(f"{self.line_index + 1}.{self.letter_line_index}")

        self.display_text.tag_remove("good", f"{self.line_index + 1}.{self.letter_line_index}",
                                     f"{self.line_index + 1}.{self.letter_line_index + 1}")
        self.display_text.tag_remove("bad", f"{self.line_index + 1}.{self.letter_line_index}",
                                     f"{self.line_index + 1}.{self.letter_line_index + 1}")
        self.display_text.tag_add("next", f"{self.line_index + 1}.{self.letter_line_index}",
                                  f"{self.line_index + 1}.{self.letter_line_index + 1}")

    def end_of_line(self):
        self.display_text.tag_remove("next", f"{self.line_index + 1}.{self.letter_line_index}",
                                     f"{self.line_index + 1}.{self.letter_line_index + 1}")
        self.letter_line_index = 1
        self.line_index += 1
        self.display_text.tag_add("next", f"{self.line_index + 1}.1", f"{self.line_index + 1}.2")

    def word_change_action(self, event_char):
        self.display_text.tag_remove("next", f"{self.line_index + 1}.{self.letter_line_index}",
                                     f"{self.line_index + 1}.{self.letter_line_index + 1}")
        if event_char == self.text[self.line_index][self.letter_line_index]:
            self.display_text.tag_add("good", f"{self.line_index + 1}.{self.letter_line_index}",
                                      f"{self.line_index + 1}.{self.letter_line_index + 1}")
        else:
            self.mistakes_index_list.append(f"{self.line_index + 1}.{self.letter_line_index}")
            self.display_text.tag_add("bad", f"{self.line_index + 1}.{self.letter_line_index}",
                                      f"{self.line_index + 1}.{self.letter_line_index + 1}")

        self.letter_line_index += 1
        self.display_text.tag_add("next", f"{self.line_index + 1}.{self.letter_line_index}",
                                  f"{self.line_index + 1}.{self.letter_line_index + 1}")

        self.char_counter += 1
