import Database

class Controller:
    def __init__(self, view):
        self.view = view
        self.correct_letter = []
        self.wrong_letter = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        #self.new_game()

    def new_game(self):
        self.word = Database.get_random_word()
        if not self.word:
            self.word = "praak"

        self.correct_letter = []
        self.wrong_letter = []
        self.attempts_left = self.max_attempts

        self.update_display()

    def send_letter(self, event=None):
        letter = self.view.text_letter.get().lower()
        if not letter:
            return
        if letter in self.correct_letter or letter in self.wrong_letter:
            self.view.text_letter.delete(0, 'end')

        if letter in self.word:
            self.correct_letter.append(letter)
        else:
            self.wrong_letter.append(letter)
            self.attempts_left -= 1


        self.update_display()
        self.check_game_end()
        self.view.text_letter.delete(0, 'end')

    def update_display(self):
        # word placeholder update
        display_word =""
        for l in self.word:
            if l in self.correct_letter:
                display_word += l + " "
            else:
                display_word += "_ "
        self.view.word_place.config(text=display_word)

        self.view.wrong_letter.config(text="Valed tähed: " + ", ".join(self.wrong_letter))

        #pic place holder
        self.view.image_box.config(text=f"[{self.max_attempts - self.attempts_left} / {self.max_attempts}]")

    def check_game_end(self):
        if all(letter in self.correct_letter for letter in self.word):
            print("ÕIGE")
            Database.save_score("Player", self.attempts_left, self.word)
            self.new_game()

        elif self.attempts_left  <= 0:
            print("EI ÕNNESTUNUD. Sõna oli: ", self.word)
            self.new_game()