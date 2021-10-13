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
# reps are the number of set i.e. 1 rep = 1(work + short break)
reps = 0
# It is the timer which will be cancelled when reset button is clicked
timer_to_cancel = None


# Time Reset
def reset():
    window.after_cancel(timer_to_cancel)
    label.config(text="TIMER")
    timer.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# Time Mechanism
def start_timer():
    global reps
    reps += 1

    # Time in seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="LONG BREAK")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="SHORT BREAK")
    else:
        count_down(work_sec)
        label.config(text="WORK")


# Countdown Mechanism
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_to_cancel
        timer_to_cancel = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "√"
        check_mark.config(text=marks)


# UI Setup
if __name__ == "__main__":
    window = Tk()
    window.config(bg=YELLOW)
    window.title("Pomodoro")
    window.minsize(height=500, width=500)

    label = Label(text="TIMER", font=FONT, highlightthickness=0, bg=YELLOW)
    label.grid(row=0, column=3)

    timer = Canvas(background=YELLOW, highlightthickness=0)
    timer_text = timer.create_text(180, 150, text="00:00", fill=RED, font=FONT)
    timer.grid(row=2, column=3)

    start_button = Button(text="Start", font=BUTTON_FONT, bg=PINK, highlightthickness=0, command=start_timer)
    start_button.grid(row=3, column=2)

    check_mark = Label(font=CHECK_MARK_FONT, fg=GREEN, bg=YELLOW, highlightthickness=0)
    check_mark.grid(row=3, column=3)

    reset_button = Button(text="Reset", font=BUTTON_FONT, bg=PINK, highlightthickness=0, command=reset)
    reset_button.grid(row=3, column=4)

    window.mainloop()
