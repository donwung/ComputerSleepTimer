import tkinter as tk

class AMPM_Entry(tk.Frame):
    def __init__(self, parent, entry_width):
        self.AMPM = "AM"
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self, borderwidth=2, relief=tk.SUNKEN)
        frame.grid(row="0", column="0")

        self.entry = tk.Entry(
            frame,
            width=entry_width,
            font=("Arial", 12),
            borderwidth=10,
            relief=tk.FLAT,
            state="disabled"
        )

        self.text = tk.Text(self, height=10, width=40)
        self.entry.grid(row="0", column="0")

        self.entry.config(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, "AM")
        self.AMPM = "AM"
        self.entry.config(state="disabled")

    def set_PM(self):
        self.entry.config(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, "PM")
        self.AMPM = "PM"
        self.entry.config(state="disabled")

    def set_AM(self):
        self.entry.config(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, "AM")
        self.AMPM = "AM"
        self.entry.config(state="disabled")

    def get(self):
        return self.AMPM