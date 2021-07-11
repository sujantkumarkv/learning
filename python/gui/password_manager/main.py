# activefill from canvas is an option to use, great one.
from tkinter import *
from tkinter import messagebox
# Though we imported * from tkinter, it only imports the classes,messagebox isn't a class.

import random
import pyperclip
# This simply allows us to automatically copy the text, here the random-password we generate.
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

LOGO_WIDTH = 200
LOGO_HEIGHT = 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_clicked():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    # The above one also works but we can reduce the code by using list comprehensions,exclusively in Python.

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)
    letters_list= [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list= [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password= "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_clicked():
    site = site_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    json_data = {
        site: {
            "username": username,
            "password": password,
        }
    }

    if len(site)==0 or len(username)==0 or len(password)==0:
        messagebox.showinfo(title="Empty Fields", message="Looks like u left the fields Empty :( Fill in !!")

    else:
        # is_ok = messagebox.askokcancel(title=f"{site}", message=f"Site- {site}\n"f"Username- {username}\nPassword- "
        #                                                         f"{password}\n Continue to Save?")
        # if is_ok:
        try:
            with open("Password_Data.json", "r") as password_data:
                #Read old data by loading it
                temp_data= json.load(password_data)
                #Updating with new data
                temp_data.update(json_data)

        except FileNotFoundError:
            with open("Password_Data.json", "w") as password_data:
                json.dump(json_data, password_data, indent=3)

        else:
            with open("Password_Data.json", 'w') as password_data:
                #Opening again, this time w.r.t writing it. Now dumping new dictionary data into *json* file. :)
                json.dump(temp_data, password_data, indent=3)

        messagebox.showinfo(title=site, message=f"Details of {site} Saved succesfully !!")
        site_entry.delete("0", END)
        username_entry.delete("0", END)
        pass_entry.delete("0", END)
        site_entry.focus()

# --------------------SEARCH BUTTON CLICKED ----------------------------- #

def search():
    sitename= site_entry.get()
    try:
        with open("Password_Data.json", "r") as password_data:
            data= json.load(password_data)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found :( ")

    else:
        if sitename in data:
            display_username= data[sitename]["username"]
            display_pass= data[sitename]["password"]
            messagebox.showinfo(title=sitename, message=f"Found !!\nUsername: {display_username}\nPassword: {display_pass}")

        else:
            messagebox.showinfo(title="Not Found", message=f"No such data exists regarding '{sitename}'.\nTry saving !!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Faaltu Password Manager")
window.config(bg=YELLOW, padx=41, pady=71)

canvas = Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT, bg=YELLOW, highlightthickness=0)
# Canvas width, height are set acc to size of our logo
logo_img = PhotoImage(file="password_manager_logo.png")
canvas.create_image(LOGO_WIDTH / 2, LOGO_HEIGHT / 2, image=logo_img)
canvas.grid(row=0, column=1)
# The above code places the logo at centre canvas (width,height)/2;using "anchor" keyword,we can chnage its position tho'
# like anchor=nw, tends to align the logo's top left corner to placed at LOGO_WIDTH/2, LOGO_HEIGHT/2.
# ///////////////////////////////////////////

site_label = Label(text="Site/App:", bg=YELLOW, font=(FONT_NAME, 11, "italic"))
site_label.grid(row=1, column=0)

username_label = Label(text="Mail/Username:", bg=YELLOW, font=(FONT_NAME, 11, "italic"))
username_label.grid(row=2, column=0)

pass_label = Label(text="Password:", bg=YELLOW, font=(FONT_NAME, 11, "italic"))
pass_label.grid(row=3, column=0)

# //////////////////////////////////

site_entry = Entry(width=32)
site_entry.grid(row=1, column=1)
site_entry.focus()

username_entry = Entry(width=43)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "example@email.com")

pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

# ////////////////////////////////////////

generate_btn = Button(text="Generate", width=8, command=generate_clicked)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=add_clicked)
add_btn.config(padx=3, pady=3)
add_btn.grid(row=5, column=1, columnspan=2)


search_btn= Button(text="Search", width=8, command=search)
search_btn.grid(row=1, column=2)

window.mainloop()
