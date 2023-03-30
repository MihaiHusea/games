#!/usr/bin/env python3
import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Dice")
window.geometry("350x300")
window.configure(background="black")
window.resizable(width=False, height=False)

img1 = ImageTk.PhotoImage(Image.open("pictures/1.png"))
img2 = ImageTk.PhotoImage(Image.open("pictures/2.png"))
img3 = ImageTk.PhotoImage(Image.open("pictures/3.png"))
img4 = ImageTk.PhotoImage(Image.open("pictures/4.png"))
img5 = ImageTk.PhotoImage(Image.open("pictures/5.png"))
img6 = ImageTk.PhotoImage(Image.open("pictures/6.png"))

label_dice_roll1 = tk.Label(window, font=('Arial', 100, 'bold'), bg='black', fg='black')
label_dice_roll1.place(x=80, y=20, width=100, height=110)
label_dice_roll2 = tk.Label(window, font=('Arial', 100, 'bold'), bg='black', fg='black')
label_dice_roll2.place(x=180, y=20, width=100, height=110)


def dice_throw():
    return random.choice([i for i in range(1, 7)])


def show_dice_faces(label):
    match dice_throw():
        case 1:
            label['image'] = img1
        case 2:
            label['image'] = img2
        case 3:
            label['image'] = img3
        case 4:
            label['image'] = img4
        case 5:
            label['image'] = img5
        case 6:
            label['image'] = img6


def dice():
    show_dice_faces(label=label_dice_roll1)
    show_dice_faces(label=label_dice_roll2)


button_dice_roll = tk.Button(
    text="throw\nthe dice",
    width=8,
    height=3,
    font=("Arial", 18, "bold"),
    bg="#285921",
    fg="black",
    command=dice)
button_dice_roll.place(x=110, y=140)

window.mainloop()
