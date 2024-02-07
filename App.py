import tkinter as tk
from Clock import Clock
from Input_Field import Input_Field
from Sleep_Manager import Sleep_Manager


window = tk.Tk()
window.title("Computer Sleep Timer - v1.0")
window.iconbitmap("icon.ico")

clock = Clock(window)
input_field = Input_Field(window)

sleep_manager = Sleep_Manager(input_field, clock)

clock.create_clock()
sleep_manager.create_sleep_settings()

window.minsize(400, 200)
window.mainloop()
