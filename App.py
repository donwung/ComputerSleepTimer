import tkinter as tk
from Clock import Clock
from Input_Field import Input_Field
from Sleep_Manager import Sleep_Manager
from Countdown import Countdown
from tkinter.font import Font


window = tk.Tk()

clock = Clock(window)
input_field = Input_Field(window)
# countdown = Countdown(window)

sleep_manager = Sleep_Manager(input_field, clock)


clock.create_clock()
sleep_manager.create_sleep_settings()
# after doing sleep settings, the input fields will appear
# countdown.create_countdown_timer()
# countdown.create_countdown_buttons()


window.minsize(400, 200)
window.mainloop()
