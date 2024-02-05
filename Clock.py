import tkinter as tk
import datetime


class Clock(tk.Frame):
    __current_time = datetime.datetime.now()
    __is_ticking = True
    __label_text = "LABEL TEXT"
    __clock = None

    def __init__(self, parent):
        self.__clock = tk.Label(
            text=self.__label_text, font=("Arial", 25), bg="black", fg="white"
        )
        self.__clock.pack(fill="x")

        # enable clock ticking on start
        self.enable_ticking()
        self.tick()
        print("Clock instantiated")

    def get_hour(self):
        hour = int(self.__current_time.hour)
        return hour

    def get_minute(self):
        minute = int(self._current_time.minute)
        return minute

    def get_second(self):
        second = int(self._current_time.second)
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
        AMPM = "AM"

        if hour == 12:
            AMPM = "PM"

        if hour > 12:
            hour_str = str(hour - 12)
        elif hour == 0:
            hour_str = "12"
            AMPM = "AM"
        else:
            hour_str = str(hour)

        if len(minute_str) < 2:
            minute_str = str(minute)
        if len(second_str) < 2:
            second_str = str(second)

        return f"{hour_str} : {minute_str} : {second_str} {AMPM}"

    def get_time_string(self, format: str):
        hour = self.get_hour()
        minute = self.get_minute()
        second = self.get_second()

        if format == "12":
            return self.time_string_12(hour, minute, second)
        if format == "24":
            return self.time_string_24(hour, minute, second)
        print("Check time format param")

    def tick(self):
        if self.__is_ticking:
            self._current_time = datetime.datetime.now()
            self.__label_text = self.get_time_string("12")

            self.__clock.config(text=self.__label_text)
            self.__clock.after(1, self.tick)
        else:
            print("is_ticking is set to false")

    def disable_ticking(self):
        self.__is_ticking = False

    def enable_ticking(self):
        self.__is_ticking = True
