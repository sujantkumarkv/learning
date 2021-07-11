from tkinter import *

window= Tk()
window.title("Faaltu sa Dist converter")
# window.minsize(width=301, height=301)
window.config(padx=11, pady=11)

def miles_to_km():
    miles= float(from_entry.get())
    km= miles * 1.609
    to_km_label.config(text=f"{km}")

from_label= Label(text="Miles")
from_label.grid(row=0, column=2)
# from_label.config(padx=11, pady=11)

to_label= Label(text="KMs")
to_label.grid(row=1, column=2)
# to_label.config(padx=11, pady=11)

equalto_label= Label(text="Equals")
equalto_label.grid(row=1, column=0)
# equalto_label.config(padx=11, pady=11)

from_entry= Entry(width=11)
from_entry.grid(row=0, column=1)
# from_entry.config(padx=11, pady=11)

to_km_label= Label()
to_km_label.grid(row=1, column=1)
# to_km_label.config(padx=11, pady=11)

calc_btn= Button(text="Calculate", command=miles_to_km)
calc_btn.grid(row=2, column=1)
# calc_btn.config(padx=11, pady=11)


window.mainloop()