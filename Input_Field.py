import tkinter as tk
from Number_Entry import Number_Entry
from AMPM_Entry import AMPM_Entry


# Input_Field is responsible for creating the primary interactible forms and fields.
# This class builds forms and returns the information on those forms.
class Input_Field:
    def __init__(self, parent):
        # print("Input_Field instantiated")
        self.pixel = tk.PhotoImage(width=1, height=1)
        self.parent = parent
        self.hours_entry = None
        self.minutes_entry = None
        self.seconds_entry = None
        self.clock_format = 24

    def create_sleep_IN_fields(self, frame):
        # print("creating IN fields")

        self.clock_format = 24
        input_field_frame = tk.Frame(frame)
        input_field_frame.pack(side="top")

        self.create_field(input_field_frame, "hour", 256)
        self.create_field(input_field_frame, "minute", 256)
        self.create_field(input_field_frame, "second", 256)

    def create_sleep_AT_fields(self, frame, clock_format):
        # print("creating AT fields")

        self.clock_format = clock_format
        input_field_frame = tk.Frame(frame)
        input_field_frame.pack(side="top")

        self.create_field(input_field_frame, "hour", clock_format)
        self.create_field(input_field_frame, "minute", 60)
        self.create_field(input_field_frame, "second", 60)
        if self.clock_format == 12:
            self.create_AMPM_radio(input_field_frame)

    def create_field(self, parent, label_name, max):
        frame = tk.Frame(parent)
        frame.pack(side="left")
        buttons = tk.Frame(frame, bg="yellow")
        entry_width = 5

        if label_name == "hour":
            self.hours_entry = Number_Entry(frame, entry_width, max)
            entry = self.hours_entry
        elif label_name == "minute":
            self.minutes_entry = Number_Entry(frame, entry_width, max)
            entry = self.minutes_entry
        elif label_name == "second":
            self.seconds_entry = Number_Entry(frame, entry_width, max)
            entry = self.seconds_entry
        else:
            raise Exception("label_name has invalid parameter")

        label = tk.Label(frame, text=label_name, width=8, justify="left", anchor="w")

        increment = tk.Button(
            buttons,
            image=self.pixel,
            height=11,
            width=25,
            compound="c",
            text="+",
            command=entry.increment,
        )
        decrement = tk.Button(
            buttons,
            image=self.pixel,
            height=11,
            width=25,
            compound="c",
            text="-",
            command=entry.decrement,
        )
        increment.pack(side="top")
        entry.pack(side="left", expand="true")
        decrement.pack(side="top")
        label.pack(side="right")
        buttons.pack(side="left")

    def create_AMPM_radio(self, parent):
        frame = tk.Frame(parent)
        frame.pack(side="left")
        buttons = tk.Frame(frame, bg="yellow")
        entry_width = 5

        self.AMPM_field = AMPM_Entry(frame, entry_width)
        AMPM_field = self.AMPM_field

        set_PM_btn = tk.Button(
            buttons,
            image=self.pixel,
            height=11,
            width=25,
            compound="c",
            text="PM",
            command=AMPM_field.set_PM,
        )
        set_AM_btn = tk.Button(
            buttons,
            image=self.pixel,
            height=11,
            width=25,
            compound="c",
            text="AM",
            command=AMPM_field.set_AM,
        )
        set_PM_btn.pack(side="top")
        AMPM_field.pack(side="left", expand="true")
        set_AM_btn.pack(side="top")
        buttons.pack(side="left")

    def get_time_dict(self):
        hour = self.hours_entry.get()
        minute = self.minutes_entry.get()
        second = self.seconds_entry.get()

        time_dict = {
            "hours": int(hour),
            "minutes": int(minute),
            "seconds": int(second),
        }

        if self.clock_format == 12:
            AMPM = self.AMPM_field.get()
            time_dict["AMPM"] = str(AMPM)

        # print(f"HOUR:{hour} MIN:{minute} SEC:{second}")
        return time_dict
