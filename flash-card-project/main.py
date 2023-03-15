from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict('records')
current_card = {}

# move to the next French card
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

# flip to the equivalent English card
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_card["English"],fill="black")
    canvas.itemconfig(card_background, image=card_back_img)
    window.after(3000, func=next_card)

#window setup
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#icons and symbols setup
canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400, 150, fill="black", text="Title", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, fill="black", text="word", font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=flip_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
