import tkinter as tk
from Clock import Clock


window = tk.Tk()

# TODO: create clock DONE!
# set a time to go to sleep IN
# TODO: create input fields for numbers
# input fields should receive hours, minutes, seconds
# these three inputs will set a timer for X milliseconds until the computer is slept

# set a time to go to sleep AT
# TODO: create input fields for numbers
# input fields should receive hours, minutes, seconds
# these three inputs will then be compared to the current time, and sleep when time is reached


clock = Clock(window)

# this is test text - irrelevant
greeting = tk.Label(text="Hello World!")
greeting.pack()

window.mainloop()
