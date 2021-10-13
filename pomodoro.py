from tkinter import *
# Constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Cambria", 20, "bold")
BUTTON_FONT = ("Cambria", 16, "bold")
CHECK_MARK_FONT = ("Cambria", 12, "bold")
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 25

# Time Reset

# Time Mechanism

# Countdown Mechanism

# UI Setup

window = Tk()
window.config(bg=YELLOW)
window.title("Pomodoro")
window.minsize(height=500, width=500)

label = Label(text="TIMER", font=FONT, highlightthickness=0, bg=YELLOW)
label.config()
label.grid(row=0, column=3)

canvas = Canvas(background=YELLOW, highlightthickness=0)
canvas.create_text(180, 150, text="00:00", fill=RED, font=FONT)
canvas.grid(row=2, column=3)

button_one = Button(text="Start", font=BUTTON_FONT, bg=PINK, highlightthickness=0)
button_one.grid(row=3, column=2)

check_mark = Label(text="√", font=CHECK_MARK_FONT, fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3, column=3)

button_two = Button(text="Reset", font=BUTTON_FONT, bg=PINK, highlightthickness=0)
button_two.grid(row=3, column=4)


window.mainloop()
