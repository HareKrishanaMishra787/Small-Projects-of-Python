from tkinter import *

def cal():
    x = float(miles.get())
    calculate = x * 1.60934
    kilometer_label.config(text = f"{calculate}")

windows = Tk()
windows.title("Miles to kilometer convertor")
windows.config(padx = 20,pady=20)

#entry
miles = Entry(width=7)
miles.grid(column = 1,row = 0)

#lables

miles_key= Label(text ="Miles")
miles_key.grid(column = 2, row = 0)

is_equal_to= Label(text = "is equal to ")
is_equal_to.grid(column = 0,row = 1)

kilometer_label = Label(text = '0')
kilometer_label.grid(column=1, row=1)

km= Label(text = "km ")
km.grid(column = 2,row = 1)



#buttons
button = Button(text ="Calculate", command=cal)
button.grid(column = 1,row = 2)

















windows.mainloop()