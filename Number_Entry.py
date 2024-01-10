import tkinter as tk
from tkinter import messagebox

class Number_Entry(tk.Frame):
    def __init__(self, parent):
        self.STR = ""
        tk.Frame.__init__(self, parent)

        vcmd = (self.register(self.onValidate), '%d',
                '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # Input and input debug
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.text = tk.Text(self, height=10, width=40)
        self.entry.grid(row="0", column="0")
        self.submit = tk.Button(self, text="Button", command=self.get)
        self.submit.grid(row="0", column="1")
        # self.text.pack(side="bottom", fill="both", expand=True)

    def onValidate(self, d, i, P, s, S, v, V, W):
        # can remove some of these
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
        if (self.STR == ""):
            print("undefined")
        else:
            print(self.STR)