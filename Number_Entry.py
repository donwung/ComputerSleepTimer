import tkinter as tk

class Number_Entry(tk.Frame):
    def __init__(self, parent, entry_width, max):
        self.STR = ""
        self.max = max
        tk.Frame.__init__(self, parent)

        vcmd = (
            self.register(self.onValidate),
            "%d",
            "%i",
            "%P",
            "%s",
            "%S",
            "%v",
            "%V",
            "%W",
        )

        frame = tk.Frame(self, borderwidth=2, relief=tk.SUNKEN)
        frame.grid(row="0", column="0")

        self.entry = tk.Entry(
            frame,
            validate="key",
            validatecommand=vcmd,
            width=entry_width,
            font=("Arial", 12),
            borderwidth=10,
            relief=tk.FLAT,
        )

        self.text = tk.Text(self, height=10, width=40)
        self.entry.grid(row="0", column="0")

        self.entry.delete(0, "end")

        if(self.max == 12):
            self.entry.bind("<KeyRelease>", self.one)
            self.entry.bind("<KeyRelease>", self.cap, add='+')
            self.entry.insert(0, "1")
        else:
            self.entry.bind("<KeyRelease>", self.zero)
            self.entry.bind("<KeyRelease>", self.cap, add='+')
            self.entry.insert(0, "0")
        # self.submit = tk.Button(self, text="Button", command=self.get)
        # self.submit.grid(row="0", column="1")
        # self.text.grid()

    def onValidate(self, d, i, P, s, S, v, V, W):
        self.text.delete("1.0", "end")
        self.text.insert("end", "OnValidate:\n")
        self.text.insert("end", "d='%s'\n" % d)
        self.text.insert("end", "i='%s'\n" % i)
        self.text.insert("end", "P='%s'\n" % P)
        self.text.insert("end", "s='%s'\n" % s)
        self.text.insert("end", "S='%s'\n" % S)
        self.text.insert("end", "v='%s'\n" % v)
        self.text.insert("end", "V='%s'\n" % V)
        self.text.insert("end", "W='%s'\n" % W)

        # Disallow anything but numbers
        if S.isnumeric():
            self.text.insert("end", "STR='%s'\n" % P)
            self.STR = P
            return True

        else:
            self.text.insert("end", "STR='%s'\n" % s)
            self.STR = s
            self.bell()
            return False

    def get(self):
        # print debug text wall
        # print(self.text.get('1.0', 'end-1c'))
        if self.STR == "":
            out = "undefined"
            # print(out)
            return out
        else:
            out = self.STR
            # print(out)
            return out

    def increment(self):
        if int(self.STR) + 1 < self.max:
            new_entry = int(self.STR) + 1
        else:
            self.bell()

        # print(new_entry)
        self.STR = new_entry
        self.entry.delete(0, "end")
        self.entry.insert(0, new_entry)

    def decrement(self):
        # case where format is 12h
        # technically, case where max time range is 12, but 12 can only occur as
        # a maximum in the hour field - other fields are 60, 60, and 1000

        if int(self.STR) - 1 <= 1 and self.max == 12:
            new_entry = 1
            self.bell()
        elif int(self.STR) >= 1:
            new_entry = int(self.STR) - 1
        else:
            new_entry = 0
            self.bell()

        # print(new_entry)
        self.STR = new_entry
        self.entry.delete(0, "end")
        self.entry.insert(0, new_entry)

    def zero(self, event):
        if self.get() == "undefined":
            self.entry.delete(0, "end")
            self.entry.insert(0, "0")

    def one(self, event):
        if self.get() == "undefined" or int(self.get()) <= 1:
            self.entry.delete(0, "end")
            self.entry.insert(0, "1")

    def cap(self, event):
        # print("reached cap")
        if int(self.get()) >= self.max and self.max == 12:
            self.entry.delete(0, "end")
            self.entry.insert(0, str(self.max))
        elif int(self.get()) >= self.max:
            self.entry.delete(0, "end")
            self.entry.insert(0, str(self.max - 1))