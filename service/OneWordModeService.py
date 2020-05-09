from service.GameService import GameService


class OneWordModeService(GameService):
    def __init__(self):
        GameService.__init__(self)
        self.current_word = None

    def get_random_word(self):
        self.current_word = self.generator.get_random_word()
        return self.current_word

    def check_word(self, word_entered):
        if self.current_word == word_entered:
            self.words_correct += 1
        else:
            self.words_incorrect += 1
        self.char_counter += (len(word_entered) + 1)


