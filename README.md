# COMPUTER SLEEP TIMER

This is an app built using Python and Tkinter to set my computer to sleep at a certain time (primarily while downloading a game overnight).

## USE

The app doesn't have that many interactive features, so I think it's pretty easy to use.

You can change whether the clock is shown in 12 Hour or 24 Hour format.

![Screenshot 2024-02-07 161557](https://github.com/donwung/ComputerSleepTimer/assets/113479299/8cc363d6-3748-4469-b908-93d2adab8e73)
![image](https://github.com/donwung/ComputerSleepTimer/assets/113479299/dfeffb91-a453-4fbb-b3ed-40bedab891e0)



And you can select whether you want to set your computer to sleep on a countdown, or on a schedule.
![image](https://github.com/donwung/ComputerSleepTimer/assets/113479299/3840196d-64f5-4eb2-a0c4-53622a2d5621)
![image](https://github.com/donwung/ComputerSleepTimer/assets/113479299/229bb97d-3d93-4c41-bc1b-ecfad0e91bed)



After setting your time, upon selection of Start Countdown, your computer will be primed to sleep under your settings.

----
### DISCLAIMER

*BE SURE TO SAVE ALL YOUR WORK*

*I AM NOT RESPONSIBLE FOR DAMAGES CAUSED BY UNEXPECTED COMPUTER SHUTDOWNS/HIBERNATIONS/ETC.*

## BUILDING

### Prerequisites:

- Python 3.X

- Pip package manager

- Pyinstaller

----

Navigate to your directory.

In Terminal: `git clone https://github.com/donwung/ComputerSleepTimer.git`

Make your changes then rerun.

In Terminal: `py App.py`

OPTIONAL: CodeRunner works, be sure to run CodeRunner on App.py

Whenever you're finished, you can run `pyinstaller --onefile --noconsole --clean --icon='icon.png' App.py` in Terminal to build your own redistributable

NOTE: Be sure the icon address is correct otherwise the app will not compile.

CONTRIBUTION

If you've got changes you'd like to add, create a fork and create a pull request at your leisure.

I probably won't pick up on it immediately, so you can expedite the process by @ing me on Discord @rearbones.

Thanks, and have fun being on a time limit!
