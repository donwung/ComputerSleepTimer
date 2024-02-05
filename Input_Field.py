import tkinter as tk
from Number_Entry import Number_Entry


class Input_Field:
    def __init__(self, parent):
        print("Input_Field instantiated")
        self.pixel = tk.PhotoImage(width=1, height=1)

        self.create_field(parent, "hours")
        self.create_field(parent, "minutes")
        self.create_field(parent, "seconds")


    def create_field(self, parent, label_name):
        frame = tk.Frame(parent)
        frame.pack(side="left")
        buttons = tk.Frame(frame, bg="yellow")

        if(label_name=="hours"):
            self.hour_entry = Number_Entry(frame, entry_width=5)
            entry = self.hour_entry
        elif(label_name=="minutes"):
            self.minutes_entry = Number_Entry(frame, entry_width=5)
            entry = self.minutes_entry
        elif(label_name=="seconds"):
            self.seconds_entry = Number_Entry(frame, entry_width=5)
            entry = self.seconds_entry
        else:
            raise Exception("label_name has invalid parameter")

        label = tk.Label(
            frame, text=label_name, width=10, justify="left", anchor="w"
        )

        def say():
            print("say")

        increment = tk.Button(
            buttons,
            image=self.pixel,
            height=11,
            width=25,
            compound="c",
            text="+",
            command=say,
        )
        increment.pack(side="top")
        entry.pack(side="left", expand="true")
        decrement = tk.Button(
            buttons, image=self.pixel, height=11, width=25, compound="c", text="-"
        )
        decrement.pack(side="top")
        label.pack(side="right")
        buttons.pack(side="left")

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
