from service.Generator import Generator

time = 60


class GameService:

    def __init__(self):
        self.generator = Generator()
        self.words_correct = 0
        self.words_incorrect = 0
        self.game_time = time
        self.time = time
        self.char_counter = 0
        self.game_active = False
        self.start_typing = False

    def start_game(self):
        self.words_correct = 0
        self.words_incorrect = 0
        self.time = time
        self.char_counter = 0
        self.game_active = True

    def stop_game(self):
        self.start_typing = False
        self.game_active = False

    def refresh_game(self):
        if self.game_active and self.time > 0:
            self.time -= 1
            return True
        elif self.time == 0:
            return False
