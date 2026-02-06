from random import choice

import Database
from tkinter import messagebox, simpledialog, Toplevel, Label


class Controller:
    def __init__(self, view):
        self.view = view
        self.correct_letter = []
        self.wrong_letter = []
        self.max_attempts = 12
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
        self.view.update_hangman_image(self.attempts_left)

    def check_game_end(self):
        # kui võidab
        if all(letter in self.correct_letter for letter in self.word):
            # küsi nime
            player_name = simpledialog.askstring("Õige!", f"Sõna oli '{self.word}'!\nSisesta oma nimi:")
            if player_name:
                Database.save_score(player_name, self.attempts_left, self.word)
            #print("ÕIGE")
            choice = messagebox.askquestion("Õige!", "Kas uus mäng?\nYes=Uus mäng, No=Vaata tulemusi")
            if choice == "yes":
                self.new_game()
            else:
                self.show_score()


        elif self.attempts_left  <= 0:
            choice = messagebox.askquestion("Ei õnnestunud!", f"Sõna oli '{self.word}'\nMida soovid teha?\nYes=Uus mäng, No=Vaata tulemusi")
            if choice == "yes":
                self.new_game()
            else:
                self.show_score()
            #print("EI ÕNNESTUNUD. Sõna oli: ", self.word)
            #self.new_game()

    def show_score(self):
        scores = Database.get_score()  # will be in Database.py
        self.view.show_scores(scores)

        #score_text = "\n".join([f"{row[2]}: {row[1]} (Sõna: {row[3]})" for row in scores])
        #messagebox.showinfo("Tulemused", score_text)