import tkinter as tk
import Sleep_Manager
import datetime


class Countdown(tk.Frame):
    # Countdown class controls tickdown timers.
    # Feed this class' functions a time dictionary and it will calculate
    # in how much time it will go to sleep.
    #
    # This class is mostly functional. Included is a create_countdown_timer()
    # function, but this does not display anything interactive.
    # It should remain "just a countdown."
    def __init__(self, parent):
        print("Countdown instantiated")
        self.parent = parent
        self.input_field = None
        self.time_dict = {"hours": 0, "minutes": 0, "seconds": 0}
        self.countdown_dict = {"hours": 0, "minutes": 0, "seconds": 0}
        self.is_decrementing = False
        self.is_ticking = False

    def create_countdown_timer(self):
        countdown_frame = tk.Frame(self.parent)
        countdown_frame.pack()

        label_text = f"remaining 0 : 0 : 0"
        self.countdown_label = tk.Label(countdown_frame, text=label_text, bg="aqua")
        self.countdown_label.pack()

    def tick(self):
        print(str(self.countdown_dict))
        if self.is_ticking == True:
            self.decrement_time()
            label_text = f"remaining {self.countdown_dict['hours']} : {self.countdown_dict['minutes']} : {self.countdown_dict['seconds']}"
            self.countdown_label.config(text=label_text)
            self.countdown_label.after(1000, self.tick)
        else:
            print("timer at 0, stopped ticking")

    def calculate_countdown_dict(self, time_dict):
        current_time = datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        current_second = current_time.second
        countdown_dict = {"hours": 0, "minutes": 0, "seconds": 0}

        if current_second > time_dict["seconds"]:
            current_second = 60 - current_second
            countdown_dict["seconds"] += current_second + time_dict["seconds"]
            countdown_dict["minutes"] += 1
        else:
            countdown_dict["seconds"] += time_dict["seconds"] - current_second

        if current_minute > time_dict["minutes"]:
            current_minute = 60 - current_minute
            countdown_dict["minutes"] += current_minute + time_dict["minutes"]
            countdown_dict["hours"] += 1
        else:
            countdown_dict["minutes"] += time_dict["minutes"] - current_minute

        if current_hour > time_dict["hours"]:
            current_hour = 24 - current_hour
            countdown_dict["hours"] += current_hour + time_dict["hours"]
        else:
            countdown_dict["hours"] += time_dict["hours"] - current_hour

        print("sleeping at:" + str(countdown_dict))

        self.countdown_dict = countdown_dict

    def start_countdown(self):

        if not self.is_ticking:
            print("Starting countdown")
            self.is_ticking = True
            self.tick()
            self.start_countdown_btn.config(text="Stop Countdown")
        else:
            self.is_ticking = False
            self.start_countdown_btn.config(text="Start Countdown")


    def decrement_time(self):
        hours = self.countdown_dict["hours"]
        minutes = self.countdown_dict["minutes"]
        seconds = self.countdown_dict["seconds"]
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
            # sleeper = Sleep_Manager()
            # sleeper.go_to_sleep()

        self.countdown_dict = {"hours": hours, "minutes": minutes, "seconds": seconds}

    def create_AT_countdown_buttons(self):
        self.start_countdown_btn = tk.Button(
            self.parent, text="Start Countdown", command=self.start_AT_countdown
        )
        self.start_countdown_btn.pack(side="right", padx="20", pady="10")

    def create_IN_countdown_buttons(self):
        set_time_input = tk.Button(
            self.parent, text="Set Countdown", command=self.set_IN_time_dict
        )
        set_time_input.pack(side="left", padx="20", pady="10")

        start_countdown = tk.Button(
            self.parent, text="Start", command=self.start_IN_countdown
        )
        start_countdown.pack(side="right", padx="20", pady="10")

    def start_AT_countdown(self):
        print("calculating AT time")
        self.time_dict = self.input_field.get_time_dict()
        if "AMPM" in self.time_dict:
            print("converting 12h time to 24h time")
            if self.time_dict["AMPM"] == "PM" and self.time_dict["hours"] < 12:
                self.time_dict["hours"] += 12
            elif self.time_dict["AMPM"] == "PM" and self.time_dict["hours"] < 12:
                self.time_dict["hours"] = 0
            del self.time_dict["AMPM"]

        self.calculate_countdown_dict(self.time_dict)
        self.start_countdown()

    def hook_to_field(self, input_field):
        print("hooking input field to countdown class")
        self.input_field = input_field
