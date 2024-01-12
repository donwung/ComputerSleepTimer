import tkinter as tk
from Number_Entry import Number_Entry


class Input_Field:
    def __init__(self, parent):
        print("Input_Field instantiated")
        tk.Label(text="set computer to go to sleep in:").pack()

        hour_frame = tk.Frame(parent, bg="red")
        hour_frame.pack()
        minute_frame = tk.Frame(parent, bg="blue")
        minute_frame.pack()
        second_frame = tk.Frame(parent, bg="green")
        second_frame.pack()

        hour_label = tk.Label(hour_frame, text="hour_label", width=15)
        hour_label.pack(side="left")

        self.hour_entry = Number_Entry(hour_frame, entry_width=10)
        self.hour_entry.pack(side="right", expand="true")

        minute_label = tk.Label(minute_frame, text="minute_label", width=15)
        minute_label.pack(side="left")

        self.minute_entry = Number_Entry(minute_frame, entry_width=10)
        self.minute_entry.pack(side="right", expand="true")

        second_label = tk.Label(second_frame, text="second_label", width=15)
        second_label.pack(side="left")

        self.second_entry = Number_Entry(second_frame, entry_width=10)
        self.second_entry.pack(side="right", expand="true")

    def get_input_time(self):
        hour = self.hour_entry.get()
        minute = self.minute_entry.get()
        seconds = self.second_entry.get()

        input_time = {
            "hours": int(hour),
            "minutes": int(minute),
            "seconds": int(seconds),
        }

        out = f"HOUR:{hour} MIN:{minute} SEC:{seconds}"
        print(out)
        return input_time
