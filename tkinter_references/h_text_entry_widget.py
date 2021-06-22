#https://www.pythontutorial.net/tkinter/tkinter-entry/
import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

#textbox = ttk.Entry(container, **options)

def main():
    root = tk.Tk()
    center_the_screen(root, 600 ,400)

    text = tk.StringVar()
    textbox = ttk.Entry(root, textvariable = text)
    textbox.pack(padx = '10', fill = 'x', expand = True)
    textbox.bind('<Return>', lambda event: return_pressed(event, root, text))
    textbox.focus()

    root.mainloop()

def return_pressed(event, root, text):
    message = ttk.Label(root, text=text.get())
    message.pack()

if __name__ == '__main__': main()