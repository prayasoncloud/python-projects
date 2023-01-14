from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, timer_card
    window.after_cancel(timer_card)
    current_card = random.choice(words)
    french_word = current_card["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(card, image=card_front)
    timer_card = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card, image=card_black)
    canvas.itemconfig(title_text, text="English", fill="white")
    english_word = current_card["English"]
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(card, image=card_black)


window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer_card = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack()

card_black = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

card = canvas.create_image(400, 263, image=card_black)
canvas.grid(column=0, row=0, columnspan=2)

# canvas.create_image(400, 263, image=card_front)
# canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 300, text="word", font=("Arial", 60, "bold"))

r_button = Button(image=right, highlightthickness=0, command=next_card)
r_button.grid(column=0, row=1)

w_button = Button(image=wrong, highlightthickness=0, command=next_card)
w_button.grid(column=1, row=1)


next_card()

window.mainloop()
