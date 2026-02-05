import Database



class Controller:
    def __init__(self, view):
        self.view = view
        self.new_game()

    def new_game(self):
        self.word = Database.get_random_word()
        if not self.word:
            self.word = "praak"

        self.guessed_letter = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        self.update_display()

    def send_letter(self, event=None):
        letter = self.view.text_letter.get().lower()
        if not letter:
            return
        if letter in self.guessed_letter:
            return

        self.guessed_letter.append(letter)
        if letter not in self.word:
            self.attempts_left -= 1

        self.update_display()
        self.check_game_end()

        self.view.text_letter.delete(0, 'end')

    def update_display(self):
        display_word =""

        for letter in self.word:
            if letter in self.guessed_letter:
                display_word += letter + " "
            else:
                display_word += "_ "

        self.view.text_box.config(state='normal')
        self.view.text_box.delete(0,'end')
        self.view.text_box.insert(0,display_word)
        self.view.text_box.config(state='disabled')

    def check_game_end(self):
        if all(letter in self.guessed_letter for letter in self.word):
            print("ÕIGE")
            Database.save_score("Player", self.attempts_left, self.word)
            self.new_game()

        elif self.attempts_left  <= 0:
            print("EI ÕNNESTUNUD. Sõna oli: ", self.word)
            self.new_game()