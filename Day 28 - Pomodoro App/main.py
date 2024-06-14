#Create a forward button, also
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", font=(FONT_NAME,32,"bold"),fg=RED, bg=YELLOW)
        count_timer(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", font=(FONT_NAME,32,"bold"),fg=PINK, bg=YELLOW)
        count_timer(short_break_sec)
    else:
        timer_label.config(text="Work", font=(FONT_NAME,32,"bold"),fg=GREEN, bg=YELLOW)
        count_timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_timer(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer = window.after(1000,count_timer,count-1)
    else:
        checkers = ""
        for _ in range(math.floor(reps/2)):
            checkers += "✅"
            check_marks.config(text=checkers)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer", font=(FONT_NAME,32,"bold"),fg=GREEN, bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(font=(FONT_NAME,10,"normal"),fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()