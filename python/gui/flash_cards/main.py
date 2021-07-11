import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
LOGO_WIDTH = 800
LOGO_HEIGHT = 530
FONT_NAME = "Courier"
COUNTDOWN_TIME= 5 #Its in seconds :()
timer= None

current_card ={} #The current_card we get is a dictionary in itself.
words_to_learn= []
#----------------------------- COUNTDOWN MECHANISM ------------------------------#

def countdown():
#Wrong implementation below.
#     canvas.itemconfig(lingo_text, text="English")
#     canvas.itemconfig(word_text, text="*")#Wasn't able to get hold of current_cards's english value here since,
#     #it's defined in next_card function. The current_card is basically a python {dictionary} so a neat trick would
#     #be to create a global current_card dictionary GLOBALLY.
# TIP :: We need to start timer as soon as window appears, so we don't need any stimulant/click to start, therefore we
# can start just after creating the window itself.no extra function definin' required as I was thinkin' earlier.
    global timer
    timer= window.after(3000, func=card_flip)
    # window.after(time_delay, function_to_run, args_of_fun_to_run) ## TIP :) ##


# ------------------------------ Read File data ---------------------------------#

reader = pandas.read_csv("data/french_words.csv")
data = reader.to_dict(orient="records")
temp_data= data
# displayed= []
# print(data)
#------------------------------ SAVE DATA -------------------------------------#



# -------------------------------- Button CLicked ---------------------------------#

def next_card():

    global current_card, timer, temp_data, words_to_learn
    #Each time we hit a new card, we need to start counting 3 seconds again,so need to firstly stop earlier one.
    window.after_cancel(timer)

    current_card = random.choice(data)
    while current_card in words_to_learn:
        current_card = random.choice(data)  # No appending/adding; simply replacing data,
        # so we can use the global dictionary many times.

    words_to_learn= data.remove(current_card)
    print(words_to_learn)
    french_word = current_card["French"]

    # while french_word in displayed:
    #     next_card()
    # displayed.append(french_word)
    # return french_word
    #Wrong Logic applied above.
    canvas.itemconfig(lingo_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(card_displayed, image=card_front_img)
    # countdown()
    timer = window.after(3000, func=card_flip)

def right_clicked():
    pass

def wrong_clicked():
    pass

def card_flip():
    global current_card
    english_word= current_card["English"]
    canvas.itemconfig(lingo_text, text="English", fill="White")
    canvas.itemconfig(word_text, text=english_word, fill="White")
    canvas.itemconfig(card_displayed, image=card_back_img)

# ---------------------------------------- UI SETUP ------------------------------------------ #
window = Tk()
window.title("Faaltu Language Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=21, pady=71)
countdown()
canvas = Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)#this last attribute - highlightthickness,
card_front_img= PhotoImage(file="images/card_front.png")                                        # it removes the borderline thus improving the UI.
card_back_img= PhotoImage(file="images/card_back.png")
card_displayed= canvas.create_image(LOGO_WIDTH/2, LOGO_HEIGHT/2, image=card_front_img)

lingo_text = canvas.create_text(LOGO_WIDTH/2, LOGO_HEIGHT/4, text="", font=(FONT_NAME, 21, "bold"))
word_text = canvas.create_text(LOGO_WIDTH/2, LOGO_HEIGHT/2, text="", font=(FONT_NAME, 11))
canvas.grid(row=0, column=0, columnspan=2)

right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)

wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()
