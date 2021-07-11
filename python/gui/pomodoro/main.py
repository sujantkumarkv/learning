from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# CANVAS DIMENSIONS set according to Dimensions of tomato image used.
CANVAS_WIDTH = 202
CANVAS_HEIGHT = 224

reps = 1  # short 4 repitions,count the iteration.
work = WORK_MIN * 60
short_break = SHORT_BREAK_MIN * 60
long_break = LONG_BREAK_MIN * 60

timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_clicked():
    window.after_cancel(timer)
    global reps
    reps = 1
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")


# reset= window.after(1000, reset_clicked)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 2 != 0:
        timer_label.config(text="25Min Work")
        countdown(work)
    elif reps == 8:
        timer_label.config(text="20Min Break")
        countdown(long_break)
    else:
        timer_label.config(text="5Min Break")
        countdown(short_break)

    reps += 1


def start_clicked():
    start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):  # count is the total no of seconds.

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # Way 2 interact with canvas elements is a bit diff as we see,
    # *canvas.itemconfig()* is required to tap in.
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
        # The above timer is an event kinda which we use to call after_cancel(timer);Since this is the the event which runs
        # in our code after 1sec interval we need to store it in a variable so that we can use it later,
        #  if we define it here,so it cant be used elsewhere therefore we declare it as a global variable.
    # Count is total seconds to run any type of timer,the above if runs till count>0,but once count==0,
    # we must call to run the timer again to continue running.
    else:
        start_timer()
        marks = ""
        checkmark.config(text="✅")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Clockwa")
window.config(bg=YELLOW, padx=51, pady=51)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 31, "bold"))
timer_label.grid(row=0, column=1)

checkmark = Label(fg=RED, bg=YELLOW, font=11)
checkmark.grid(row=3, column=1)

start_btn = Button(text="Start", command=start_clicked)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", command=reset_clicked)
reset_btn.grid(row=2, column=2)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
# Without keyword *higlightthickness=0* ;We get a border outside the image canvas which doesn't look good.
BG_PIC = PhotoImage(file="tomato.png")
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=BG_PIC)
timer_text = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text="00:00", font=(FONT_NAME, 21, "bold"))
canvas.grid(row=1, column=1)
# canvas.pack()


window.mainloop()
