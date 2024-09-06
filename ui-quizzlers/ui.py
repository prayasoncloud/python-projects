from tkinter import *
THEME_COLOR = "#375362"

class QuizeInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=8, column=1)

        self.canvas = Canvas(width=300, height= 400, bg="white")

        self.question_text = self.canvas.create_text()


        self.window.mainloop()