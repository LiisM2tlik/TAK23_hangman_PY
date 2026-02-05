from tkinter import *
from tkinter import Tk, Button, Entry, Label




class View(Tk):
    def __init__(self):
        super().__init__()

        self.controller = None
        self.__width = 600
        self.__height = 600

        self.title('HANGMAN')
        self.center_window(self.__width,self.__height)

        self.top_frame = self.create_top_frame()
        self.middle_frame = self.create_middle_frame()
        self.bottom_frame = self.create_bottom_frame()

        #spliting middle frame for better view
        self.middle_left = Frame(self.middle_frame, bg='lightblue')
        self.middle_left.pack(side='left', fill='y', expand=True)

        self.middle_right = Frame(self.middle_frame, bg='lightgreen')
        self.middle_right.pack(side='right', fill='y', expand=True)

       ## self.btn_send, self.text_box, self.text_letter, self.features = self.create_frame_features()
        self.create_widgets()
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

    def create_widgets(self):
    ##def create_frame_features(self) -> tuple[Button, Entry, Entry, Label]:

        lbl_info1 =Label(self.top_frame, text='Paku täht:')
        lbl_info1.pack(side=LEFT, padx=5, pady=5)

        self.text_letter = Entry(self.top_frame, width=20)
        self.text_letter.pack(side=LEFT, padx=5, pady=5)
        self.text_letter.focus_set()

        self.btn_send = Button(self.top_frame, text='Arva', command=lambda: self.controller.send_letter())
        ##btn_send = Button(self.middle_frame, text='Paku täht', command=self.Controller.send_letter())
        self.btn_send.pack(side=LEFT, padx=5, pady=5)

        #word placeholder
        self.word_place = Label(self.middle_left,
            text="_ _ _ _ _",  # placeholder, controller updates it
            font=("Helvetica", 24),
            bg="lightblue"
        )
        self.word_place.pack(padx=5, pady=5)

        #image placeholder
        self.image_box = Label(self.middle_right,
            text="[Hangman Image]",
            bg="lightblue",
            font=("Helvetica", 20)
        )
        self.image_box.pack(padx=5, pady=5)

        # valed tähed
        self.wrong_letter = Label(self.bottom_frame,
            text="Vale tähed: ",
            bg="lightgreen",
            font=("Helvetica", 14)
        )
        self.wrong_letter.pack(padx=5, pady=5)

    def send(self, event=None):
        if self.controller:
            self.controller.send_letter()
            ##
        ##        letter = self.text_letter.get()

        ##self.text_box.config(state='normal')
        ##self.text_box.insert(END, letter + "\n")
        ##self.text_box.config(state='disabled')

        ##self.text_letter.delete(0, END)