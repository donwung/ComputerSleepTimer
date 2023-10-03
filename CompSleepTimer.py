import tkinter as tk
from tkinter import messagebox
import os
import ctypes
import datetime
import time

# initialize Tk
window = tk.Tk()



def radio():
    selection = "You selected to "
    if(radio_option.get()):
        selection = selection + " sleep from a timer."
    else:
        selection = selection + " sleep at a specified time."
    option_label.config(text = selection)

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




# label
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()



currenttime = tk.Label(text = datetime.datetime.now())
currenttime.pack()

sleeptimelabel = tk.Label(
    text="In how many ms would you like to sleep your computer?")
sleeptimelabel.pack()
sleeptime = tk.Entry(width=25)
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
testbtn = tk.Button(
    text="Set To Sleep",
    width=20,
    height=5,
    command=printtext)
testbtn.pack()

testbtn2 = tk.Button(
    text="Testing if cmd works",
    command=cmdtest
)
testbtn2.pack()

def clock():
    currenttime.config(text=datetime.datetime.now())
    currenttime.after(1000, clock)

option_label = tk.Label(window)
option_label.pack()

clock()

# start tkinter
window.mainloop()

# while(True):
#     time.sleep(2)
#     window.update()