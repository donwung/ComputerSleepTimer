import os
import ctypes
import tkinter as tk
from Countdown import Countdown


class Sleep_Manager:
    # Sleep_Manager manages the fields that influence how sleeping is performed:
    # whether it's through setting IN vs AT times.
    # Sleep_Manager also creates the forms that determine which function to use.
    # Sleep_Manager's primary function is to set the computer to sleep via go_to_sleep().
    # 
    # This class receives an input_field object and a clock to make certain forms.
    # The input forms require a clock's 12h vs 24h format to create the correct form.
    def __init__(self):
        print("Created mini manager - this constructor should be refactored out")

    def __init__(self, input_field, clock):
        print("Sleep_Manager instantiated")
        self.input_field = input_field
        self.time_dict = {"hours": 0, "minutes": 0, "seconds": 0}
        self.countdown_str = "countdown string"
        self.sleep_method = "IN"
        self.clock = clock

    def set_time_input(self):
        print("receiving a time")
        new_time = self.input_field.get_time_dict()
        self.time_dict = new_time
        print(self.time_dict)

    def get_time_input(self):
        return self.time_dict

    def convert_to_ms(self, time_dict):
        hours_to_ms = int(time_dict["hours"]) * 3600000
        minutes_to_ms = int(time_dict["minutes"]) * 60000
        seconds_to_ms = int(time_dict["seconds"]) * 1000
        # print(f"{str(time_dict['hours'])} hour -> {hours_to_ms} milliseconds")
        # print(f"{str(time_dict['minutes'])} hour -> {minutes_to_ms} milliseconds")
        # print(f"{str(time_dict['seconds'])} hour -> {seconds_to_ms} milliseconds")

        time_to_sleep_in_ms = hours_to_ms + minutes_to_ms + seconds_to_ms
        # print(time_to_sleep_in_ms)
        return time_to_sleep_in_ms

    def go_to_sleep(self):
        print("COMPUTER IS BEING PUT TO SLEEP - GOODNIGHT")
        # os.system('cmd /c "cmd going to sleep"')
        # ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

    def select_sleep_method(self):
        self.sleep_method = self.sleep_method_radio.get()
        for widget in self.sleep_input_frame.winfo_children():
            widget.destroy()
        if self.sleep_method == "IN":
            print("creating sleep IN")
            self.create_sleep_IN_fields(self.sleep_input_frame)
        if self.sleep_method == "AT":
            print("creating sleep AT")
            self.create_sleep_AT_fields(
                self.sleep_input_frame, self.clock.clock_format.get()
            )

    def create_sleep_settings(self):
        self.sleep_method_radio = tk.StringVar(None, self.sleep_method)

        sleep_IN_header = tk.Radiobutton(
            text="Set computer to sleep IN a specified time",
            variable=self.sleep_method_radio,
            value="IN",
            command=self.select_sleep_method,
        )
        sleep_AT_header = tk.Radiobutton(
            text="Set computer to sleep AT a specified time",
            variable=self.sleep_method_radio,
            value="AT",
            command=self.select_sleep_method,
        )
        sleep_IN_header.pack()
        sleep_AT_header.pack()

        self.sleep_input_frame = tk.Frame()
        self.sleep_input_frame.pack()

    def create_sleep_AT_fields(self, frame, clock_format):
        self.input_field.create_sleep_AT_fields(frame, clock_format)
        countdown = Countdown(frame)
        countdown.create_countdown_timer()
        countdown.create_AT_countdown_buttons()
        countdown.hook_to_field(self.input_field)

    def create_sleep_IN_fields(self, frame):
        self.input_field.create_sleep_IN_fields(frame)