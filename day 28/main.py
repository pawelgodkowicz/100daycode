from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def time_reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=YELLOW)


def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min:02d}:{count_sec:02d}')
    if count >= 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sesion = math.floor(reps / 2)
        for _ in range(work_sesion):
            marks += "✔"
        check_mark.config(text=marks)


window = Tk()
window.title("Pearmer")
window.config(padx=50, pady=100, bg=GREEN)

title_label = Label(text="Timer", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 35, 'bold'))
title_label.grid(row=0, column=1)

canvas = Canvas(width=256, height=256, bg=GREEN, highlightthickness=False)
pear_image = PhotoImage(file="123.png")
canvas.create_image(128, 128, image=pear_image)
timer_text = canvas.create_text(128, 168, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

button_start = Button(text="Start",
                      highlightthickness=False,
                      bg=GREEN, bd=0,
                      activebackground=GREEN,
                      activeforeground=PINK,
                      command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text='Reset',
                      highlightthickness=False,
                      bg=GREEN, bd=0,
                      activebackground=GREEN,
                      activeforeground=PINK,
                      command=time_reset)
button_reset.grid(row=2, column=2)

check_mark = Label(fg=YELLOW, bg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()
# ✔
