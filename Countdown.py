import tkinter as tk
import Sleep_Manager

class Countdown(tk.Frame):
    def __init__(self, parent, sleeper):
        print("Countdown instantiated")
        self.sleeper = sleeper
        self.parent = parent
        self.time_dict = {"hours": 0, "minutes": 0, "seconds": 0}
        self.is_decrementing = None
        self.is_ticking = False

        countdown_frame = tk.Frame(parent)
        countdown_frame.pack()

        label_text = f"remaining {self.time_dict['hours']} : {self.time_dict['minutes']} : {self.time_dict['seconds']}"
        self.countdown_label = tk.Label(countdown_frame, text=label_text, bg="aqua")
        self.countdown_label.pack()

    def tick(self):
        if self.is_ticking == True:
            print("tick")
            self.decrement_time()

            label_text = f"remaining {self.time_dict['hours']} : {self.time_dict['minutes']} : {self.time_dict['seconds']}"
            self.countdown_label.config(text=label_text)
            self.countdown_label.after(1000, self.tick)
        else:
            print("timer at 0, stopped ticking")

    def start_countdown(self):
        self.set_time_input()
        self.time_dict = self.sleeper.start_countdown()
        self.is_ticking = True
        self.tick()

    def update_display(self):
        dict = self.sleeper.get_time_input()

        hours = dict["hours"]
        minutes = dict["minutes"]
        seconds = dict["seconds"]

        label_text = f"remaining {hours} : {minutes} : {seconds}"
        self.countdown_label.config(text=label_text)

    def decrement_time(self):
        hours = self.time_dict["hours"]
        minutes = self.time_dict["minutes"]
        seconds = self.time_dict["seconds"]
        self.is_decrementing = True

        seconds = seconds - 1
        if seconds < 0:
            seconds = 59
            minutes = minutes - 1

        if minutes < 0:
            minutes = 59
            hours = hours - 1

        if hours < 0:
            # ran outta time
            hours = 0
            minutes = 0
            seconds = 0
            self.is_decrementing = False

        if self.is_decrementing == False:
            self.is_ticking = False
            # put computer to sleep here
            self.sleeper.go_to_sleep()

        self.time_dict = {"hours": hours, "minutes": minutes, "seconds": seconds}

    def set_time_input(self):
        self.sleeper.set_time_input()
        self.update_display()