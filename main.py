import csv
import random
from tkinter import *

BG = "#f5fedc"
FONT_NAME = "times new roman"
timer = None

word_list = []
display_list = []
typed_list = []


with open(file="words.csv", newline="") as words:
    words_read = csv.reader(words)
    for each_line in words_read:
        for each_word in each_line:
            word_list.append(each_word)


def count_down(count):
    global timer
    timer = window.after(1000, count_down, count - 1)

    if count > 0:
        timer_canvas.itemconfig(timer_text, text=f"{count}")
        if count < 10:
            timer_canvas.itemconfig(timer_text, text=f"0{count}")
    else:
        reset_timer()


def reset_timer():
    window.after_cancel(timer)
    timer_canvas.itemconfig(timer_text, text="00")
    title_label.config(text="TIME UP!")
    entry.unbind('<space>')
    word_comparison()


def return_entry(event):
    display_words()
    content = entry.get()
    typed_list.append(content.strip())
    entry.delete(0, END)


def word_comparison():
    correctly_typed = 0
    zipped = zip(display_list, typed_list)
    zipped_list = list(zipped)
    for each_tuple in zipped_list:
        if each_tuple[0] == each_tuple[1]:
            correctly_typed += 1
    words_canvas.itemconfig(words_to_display, text=f"You were able to type "
                                                   f"{correctly_typed} of the words correctly in one minute",
                            font=("Helvetica", 25, "normal"))


def display_words():
    entry.bind('<space>', return_entry)
    global word_list
    display_word = random.choice(word_list)
    display_list.append(display_word)
    words_canvas.itemconfig(words_to_display, text=f"{display_word}")


def clear_entry():
    entry.delete(0, END)


window = Tk()
window.title("TYPE SPEED!")
window.state("zoomed")
window.config(bg=BG)


title_label = Label(text="How Many Words Can You Type in One Minute?", bg=BG, font=(FONT_NAME, 26, "bold"))
title_label.pack()

timer_canvas = Canvas(width=100, height=104, bg=BG, highlightthickness=0)
timer_text = timer_canvas.create_text(50, 50, text="60", font=("Courier", 35, "normal"))
timer_canvas.pack()

words_canvas = Canvas(width=900, height=400, bg="#FEDCF5", highlightthickness=0)
words_to_display = words_canvas.create_text(450, 200, text="", font=("Helvetica", 90, "normal"))
words_canvas.pack()

entry = Entry(window, width=149, justify='center')
entry.focus()
entry.pack(pady=10)

start_button = Button(text="START", bg="#DCF5FE", font=("Courier", 12, "normal"),
                      command=lambda: [count_down(10), display_words(), clear_entry()])
start_button.config(width=50)
start_button.pack()

window.mainloop()
