from words import word_list
import tkinter.messagebox
from time import time
from tkinter import *
import random

TITLE_FONT = "Times New Roman"
TITLE = "blue4"
WORD_FONT = "Sans Serif"
WORD = "steel blue"
BACKGROUND = "gainsboro"
NEW_WORD = random.choice(word_list)
CORRECT_WORDS = 0
START = time()


def change_word():
    """Go to the next word"""
    global NEW_WORD
    NEW_WORD = random.choice(word_list)
    entry_box.delete(0, END)
    word.config(text=f"{NEW_WORD}")


def callback(sv):
    global NEW_WORD, CORRECT_WORDS
    current_letter = len(sv.get()) - 1
    while not time() <= START + 30:
        tkinter.messagebox.showinfo("Results", f"The results are in, you type at {(CORRECT_WORDS / 5) / 0.5} WPM.")
        break
    if sv.get() == NEW_WORD:
        CORRECT_WORDS += len(NEW_WORD)
        change_word()
    elif sv.get():
        try:
            if sv.get()[current_letter] != NEW_WORD[current_letter]:
                word.config(text=f"{NEW_WORD}", bg="Red")
            else:
                word.config(text=f"{NEW_WORD}", bg=BACKGROUND)
        except IndexError:
            word.config(text=f"{NEW_WORD}", bg="Red")


tk = Tk()
tk.title('Typing Test')
tk.config(padx=25, pady=25, bg=BACKGROUND)
tk.geometry("750x500")

title = Label(text="Typing Test", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=BACKGROUND)
title.place(relx=0.5, rely=0.1, anchor=CENTER)

word = Label(text=f"{NEW_WORD}", font=(WORD_FONT, 44), fg=WORD, bg=BACKGROUND)
word.place(relx=0.5, rely=0.5, anchor=CENTER)

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
entry_box = Entry(tk, width=15, font=(f"{WORD_FONT}", 24), textvariable=sv)
entry_box.place(relx=0.5, rely=0.7, anchor=CENTER)
entry_box.focus()
tk.mainloop()
