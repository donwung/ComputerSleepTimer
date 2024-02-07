import tkinter as tk
import datetime


class Clock(tk.Frame):
    def __init__(self, parent):
        self.current_time = datetime.datetime.now()
        self.is_ticking = False
        self.label_text = ""
        self.clock = None
        self.AMPM = "AM"
        self.parent = parent
        self.clock_format = tk.IntVar(None, 24)
        # print("Clock instantiated")

    def create_clock(self):
        self.clock = tk.Label(
            self.parent,
            text=self.label_text,
            font=("Arial", 25),
            bg="black",
            fg="white",
        )
        self.clock.pack(fill="x", side="top")

        self.clock_format_frame = tk.Frame(self.parent)
        self.clock_format_frame.pack(fill="x", side="top", expand=False)
        self.create_format_swapper()

        self.enable_ticking()
        self.tick()

    def get_hour(self):
        hour = int(self.current_time.hour)
        return hour

    def get_minute(self):
        minute = int(self.current_time.minute)
        return minute

    def get_second(self):
        second = int(self.current_time.second)
        return second

    def time_string_24(self, hour, minute, second):
        hour_str = str(hour)
        minute_str = str(minute)
        second_str = str(second)

        if len(hour_str) < 2:
            hour_str = "0" + hour_str
        if len(minute_str) < 2:
            minute_str = "0" + minute_str
        if len(second_str) < 2:
            second_str = "0" + second_str

        return f"{hour_str} : {minute_str} : {second_str}"

    def time_string_12(self, hour, minute, second):
        hour_str = ""
        minute_str = ""
        second_str = ""

        if hour == 12:
            self.AMPM = "PM"

        if hour > 12:
            hour_str = str(hour - 12)
            self.AMPM = "PM"
        elif hour == 0:
            hour_str = "12"
        else:
            hour_str = str(hour)

        if len(minute_str) < 2:
            minute_str = str(minute)
        if len(second_str) < 2:
            second_str = str(second)

        return f"{hour_str} : {minute_str} : {second_str} {self.AMPM}"

    def get_time_string(self, format):
        hour = self.get_hour()
        minute = self.get_minute()
        second = self.get_second()

        if format == 12:
            return self.time_string_12(hour, minute, second)
        if format == 24:
            return self.time_string_24(hour, minute, second)
        # print("Check time format param")

    def tick(self):
        if self.is_ticking:
            self.current_time = datetime.datetime.now()
            self.label_text = self.get_time_string(self.clock_format.get())

            self.clock.config(text=self.label_text)
            self.clock.after(1, self.tick)
        else:
            print("is_ticking is set to false")

    def disable_ticking(self):
        self.is_ticking = False

    def enable_ticking(self):
        self.is_ticking = True

    def create_format_swapper(self):
        clock_12 = tk.Radiobutton(
            self.clock_format_frame,
            text="12h Format",
            variable=self.clock_format,
            value=12,
            bg="white",
            command=self.clock_format.set(12),
        )
        clock_24 = tk.Radiobutton(
            self.clock_format_frame,
            text="24h Format",
            variable=self.clock_format,
            value=24,
            bg="white",
            command=self.clock_format.set(24),
        )
        clock_12.pack(side="top", fill="x")
        clock_24.pack(side="top", fill="x")