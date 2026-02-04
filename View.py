from tkinter import *
from tkinter import Tk, Button, Entry, Label

import controller


class View(Tk):
    def __init__(self):
        super().__init__()
        self.controller = controller
        self.__width = 600
        self.__height = 600

        self.title('HANGMAN')
        self.center_window(self.__width,self.__height)

        self.top_frame = self.create_top_frame()
        self.middle_frame = self.create_middle_frame()
        self.bottom_frame = self.create_bottom_frame()

        self.btn_send, self.text_box, self.text_letter, self.features = self.create_frame_features()

        self.bind('<Return>', self.send)

    def main(self):
        self.mainloop()

    def center_window(self,width,height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, bg='grey', height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_middle_frame(self):
        frame = Frame(self, bg='lightblue', height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='lightgreen', height=15)
        frame.pack(expand=True, fill=X)
        return frame


    def create_frame_features(self) -> tuple[Button, Entry, Entry, Label]:

        lbl_info1 =Label(self.middle_frame, text='Paku täht')
        lbl_info1.grid(row=0, column=0, padx=5, pady=5)

        text_letter = Entry(self.middle_frame, width=20)
        text_letter.grid(row=0, column=1, padx=5, pady=5)
        text_letter.focus_set()

        btn_send = Button(self.middle_frame, text='Send', command=self.send)
        btn_send.grid(row=0, column=2, padx=5, pady=5)

        lbl_info2 = Label(self.bottom_frame, text='Pakutud')
        lbl_info2.grid(row=0, column=1, padx=5, pady=5)

        text_box = Entry(self.bottom_frame, state='disabled', width=20)
        text_box.grid(row=1, column=1, padx=5, pady=5)

        image_box = Label(self.middle_frame, text='Pildikoht')
        image_box.grid(row=0, column=3, padx=5, pady=5)

        return btn_send, text_box, text_letter, image_box

    def send(self, event=None):
        letter = self.text_letter.get()

        self.text_box.config(state='normal')
        self.text_box.insert(END, letter + "\n")
        self.text_box.config(state='disabled')

        self.text_letter.delete(0, END)