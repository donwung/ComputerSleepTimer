import tkinter as tk
from tkinter import messagebox
import os
import ctypes
import datetime
import time
import threading

# initialize Tk
window = tk.Tk()


class Number_Entry(tk.Frame):
    def __init__(self, parent):
        self.STR = ""
        tk.Frame.__init__(self, parent)

        vcmd = (self.register(self.onValidate), '%d',
                '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.text = tk.Text(self, height=10, width=40)
        self.entry.pack(side="top", fill="x")
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


def radio():
    # this creates a new widget, placed *after* all other created widgets (it appears at the bottom always)
    # create and package a label
    option_label = tk.Label(window, text="Testing")
    option_label.pack()

    
    selection = "You selected to "
    if (radio_option.get()):
        _selection = selection + " sleep from a timer."
    else:
        _selection = selection + " sleep at a specified time."
    option_label.config(text=_selection)

    # remove label after 2000 ms
    window.after(2000, option_label.destroy)




def enable_sleep(sleep):
    if (int(sleep) > 300000):
        messagebox.showinfo(
            "Sleep Enabled", "Your computer is set to sleep in " + sleep + "ms")
    else:
        messagebox.showerror(
            "Sleep Not Enabled", "Please enter a reasonable time to sleep your computer (more than 300000ms).")


def invalid_input():
    messagebox.showerror("Invalid Time", "Enter a valid time in ms.")


# parse input
def printtext():
    print("Disabling current sleep timer...")
    sleep = sleeptime.get()
    # print("parsing input: " + sleep)
    if (sleep.isnumeric()):
        print("sleeping in " + sleep + "ms")
        enable_sleep(sleep)
    else:
        print("not a valid ms input!")
        invalid_input()


def cmdtest():
    print("testing cmd")
    # os.system('cmd /c "echo Hello World!"')
    # don't use shutdown -- it doesn't allow sleep
    # os.system('cmd /c "psshutdown -d -t 20"')

    # this command is probably most ideal
    # but I will have TODO: a countdown timer on the GUI
    # and have a confirmation prompt on closing the GUI
    # ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)


####################
####################
####################
####################
# label
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()


currenttime = tk.Label(text=datetime.datetime.now())
currenttime.pack()

sleeptimelabel = tk.Label(
    text="In how many ms would you like to sleep your computer?")
sleeptimelabel.pack()
sleeptime = Number_Entry(window)
sleeptime.pack()


radio_option = tk.IntVar()
sleep_in_time = tk.Radiobutton(
    window, text="Sleep starting from a timer.",
    variable=radio_option,
    value=0,
    command=radio)
sleep_in_time.pack()
sleep_at_time = tk.Radiobutton(
    window, text="Sleep at a specified time.",
    variable=radio_option,
    value=1,
    command=radio)
sleep_at_time.pack()


# button
# testbtn = tk.Button(
#     text="Set To Sleep",
#     width=20,
#     height=5,
#     command=printtext)
# testbtn.pack()

testbtn2 = tk.Button(
    text="Prints number in Entry field",
    command=sleeptime.get
)
testbtn2.pack()


def clock():
    currenttime.config(text="Current time: " +
                       str(datetime.datetime.now().hour) + ":" +
                       str(datetime.datetime.now().minute) + ":" +
                       str(datetime.datetime.now().second))
    currenttime.after(1000, clock)


# option_label = tk.Label(window)
# option_label.pack()

clock()


# start tkinter
window.mainloop()
