import tkinter as tk
from tkinter import messagebox
import datetime


class Clock(tk.Frame):
    __current_time = datetime.datetime.now()
    __is_ticking = True
    __label_text = "LABEL TEXT"
    __clock = None

    def __init__(self, parent):
        self.__clock = tk.Label(text=self.__label_text)
        self.__clock.pack()

        # enable clock ticking on start
        self.enable_ticking()
        self.tick()
        print("Clock instantiated")

    def get_hour(self):
        hour = str(self.__current_time.hour)
        return hour

    def get_minute(self):
        minute = str(self._current_time.minute)
        return minute

    def get_second(self):
        second = str(self._current_time.second)
        return second

    def tick(self):
        if self.__is_ticking:
            self._current_time = datetime.datetime.now()
            self.__label_text = f"HOUR: {self.get_hour()} MIN: {self.get_minute()} SEC: {self.get_second()}"

            self.__clock.config(text=self.__label_text)
            self.__clock.after(1000, self.tick)
        else:
            print("is_ticking is set to false")

    def disable_ticking(self):
        self.__is_ticking = False

    def enable_ticking(self):
        self.__is_ticking = True
