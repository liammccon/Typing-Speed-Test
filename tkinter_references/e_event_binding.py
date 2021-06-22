#https://www.pythontutorial.net/tkinter/tkinter-event-binding/
import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

def main():
    root = tk.Tk()
    center_the_screen(root)


    def return_pressed(event):
        print('Return key pressed')


    def button_clicked(event):
        message = ttk.Label(root, text='Mm click again!')
        message.pack()

    btn = ttk.Button(root, text='hey click me')
    btn.bind('<Return>', return_pressed)
    btn.bind('<Button>', button_clicked, add = '+')

    btn.focus()
    btn.pack(expand=True)


    root.mainloop()

if __name__ == '__main__': main()