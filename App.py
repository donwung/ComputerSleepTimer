import tkinter as tk
from Clock import Clock
from Input_Field import Input_Field
from Sleep_Manager import Sleep_Manager
from Countdown import Countdown
from tkinter.font import Font


window = tk.Tk()

clock = Clock(window)
input_field = Input_Field(window)
sleeper = Sleep_Manager(input_field, clock)
countdown = Countdown(window, sleeper)


clock.create_clock()
sleeper.create_sleep_controls()
countdown.create_countdown_timer()


set_time_input = tk.Button(text="Set Time", command=countdown.set_time_input)
set_time_input.pack(side="left", padx="20", pady="10")

start_countdown = tk.Button(text="Start", command=countdown.start_countdown)
start_countdown.pack(side="right", padx="20", pady="10")

window.minsize(400, 200)
window.mainloop()
