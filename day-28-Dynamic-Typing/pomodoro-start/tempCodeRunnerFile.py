from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", foreground=GREEN)
    reps = 0
    check_mark.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60  
    
    reps += 1
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", foreground=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Short Break", foreground=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", foreground=RED)
        check_mark.config()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def number_padding(number):
    if number < 10:
        number = f"0{number}"
    return number

def count_down(count):
    global timer
    timer_minutes = math.floor(count / 60) 
    timer_seconds = count % 60
    timer_minutes_00 = number_padding(timer_minutes)
    timer_seconds_00 = number_padding(timer_seconds)

    canvas.itemconfig(timer_text, text=f"{timer_minutes_00}:{timer_seconds_00}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="day-28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title
title = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40))
title.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Check mark
check_mark = Label(text="", foreground=GREEN, background=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()