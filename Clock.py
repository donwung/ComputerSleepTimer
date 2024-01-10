import tkinter as tk
from tkinter import messagebox
import datetime


class Clock(tk.Frame):
    current_time = datetime.datetime.now()
    is_ticking = True
    label_text = "LABEL TEXT"
    clock = None

    def __init__(self, parent):
        self.clock = tk.Label(text=self.label_text)
        self.clock.pack()

        # enable clock ticking on start
        self.enable_ticking()
        self.tick()
        print("creating a clock")

    def get_hour(self):
        hour = str(self.current_time.hour)
        return hour

    def get_minute(self):
        minute = str(self.current_time.minute)
        return minute

    def get_second(self):
        second = str(self.current_time.second)
        return second

    def tick(self):
        if self.is_ticking:
            self.current_time = datetime.datetime.now()
            self.label_text = f"HOUR: {self.get_hour()} MIN: {self.get_minute()} SEC: {self.get_second()}"

            self.clock.config(text=self.label_text)
            self.clock.after(1000, self.tick)
        else:
            print("is_ticking is set to false")

    def disable_ticking(self):
        self.is_ticking = False

    def enable_ticking(self):
        self.is_ticking = True
