import tkinter as tk
from Clock import Clock
from Input_Field import Input_Field
from Sleep_Manager import Sleep_Manager
from Countdown import Countdown


window = tk.Tk()


# TODO: create clock DONE!
# set a time to go to sleep IN
# TODO: create input fields for numbers DONE!
# input fields should receive hours, minutes, seconds
# these three inputs will set a timer for X milliseconds until the computer is slept
#
# sudo:
# get a time (eg 2 minutes)
# set target_time to now + 2 minutes
# set a countdown from 2 minutes
# if countdown == 0, go to sleep

# set a time to go to sleep AT
# TODO: create input fields for numbers
# input fields should receive hours, minutes, seconds
# these three inputs will then be compared to the current time, and sleep when time is reached
#
# sudo:
# get a time (2PM)
# calculate difference between now_time and target_time (2PM)
# using the calculated time, set a countdown from that time
# if countdown == 0, go to sleep

# TODO: create a time remaining + countdown timer widget

# clock only tells time
# there's no real functionality to clock besides turning it on/off
clock = Clock(window)
hms_input_field = Input_Field(window)
sleeper = Sleep_Manager(hms_input_field)


countdown = Countdown(window, sleeper)

set_time_input = tk.Button(text="set_time_input", command=countdown.set_time_input)
set_time_input.pack()

start_countdown = tk.Button(text="start_countdown", command=countdown.start_countdown)
start_countdown.pack()

window.mainloop()
