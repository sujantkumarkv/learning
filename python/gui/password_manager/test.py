from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
LOGO_WIDTH = 800
LOGO_HEIGHT = 530
FONT_NAME = "Courier"

# ------------------------------ Read File data ---------------------------------#
temp_data = pandas.read_csv("data/french_words.csv")
data = pandas.DataFrame.to_dict(temp_data, orient="records")
displayed = []


# -------------------------------- Button CLicked ---------------------------------#

# print(data)
# print(data[1]["English"])
def remove_word(index, display_data):
    temp= display_data.remove(index)
    return temp

def next_card():
    pass


def right_clicked():
    global displayed
    index = random.choice(displayed)
    french_word = index["French"]
    canvas.itemconfig(lingo_text, text="French")
    canvas.itemconfig(word_text, text=french_word)
    display_data = remove_word(index=index, display_data=display_data)
    print(index)
    print("*****************************************************")
    print(display_data)

def wrong_clicked():
    pass


# --------------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Faaltu Language Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=21, pady=71)

canvas = Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(LOGO_WIDTH / 2, LOGO_HEIGHT / 2, image=card_front_img)

lingo_text = canvas.create_text(LOGO_WIDTH / 2, LOGO_HEIGHT / 4, text="ek text", font=(FONT_NAME, 21, "bold"))
word_text = canvas.create_text(LOGO_WIDTH / 2, LOGO_HEIGHT / 2, text="ek aur text", font=(FONT_NAME, 11))
canvas.grid(row=0, column=0, columnspan=2)

right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_clicked)
right_btn.grid(row=1, column=1)

wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_clicked)
wrong_btn.grid(row=1, column=0)

window.mainloop()
