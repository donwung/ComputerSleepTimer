import tkinter as tk
from Clock import Clock
from Input_Field import Input_Field
from Sleep_Manager import Sleep_Manager


window = tk.Tk()


# TODO: create clock DONE!
# set a time to go to sleep IN
# TODO: create input fields for numbers DONE!
# input fields should receive hours, minutes, seconds
# these three inputs will set a timer for X milliseconds until the computer is slept

# set a time to go to sleep AT
# TODO: create input fields for numbers
# input fields should receive hours, minutes, seconds
# these three inputs will then be compared to the current time, and sleep when time is reached


clock = Clock(window)
hms_input_field = Input_Field(window)
sleeper = Sleep_Manager(hms_input_field)


receive_time_input = tk.Button(text="receive_time_input", command=sleeper.receive_time)
receive_time_input.pack()

test_go_to_sleep = tk.Button(text="test_go_to_sleep", command=sleeper.go_to_sleep)
test_go_to_sleep.pack()



# this is test text - irrelevant
# greeting = tk.Label(text="Hello World!")
# greeting.pack()

window.mainloop()
