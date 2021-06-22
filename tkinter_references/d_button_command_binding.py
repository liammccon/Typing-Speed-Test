#https://www.pythontutorial.net/tkinter/tkinter-command/
import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

def main():
    root = tk.Tk()
    center_the_screen(root, 600 ,400)

    # the function called when button is clicked. Notice it is in main scope!
    #thats because if you pass args with (root) it would be called right away
    def button1_clicked():
        message = ttk.Label(root, text='Button clicked!!')
        message.pack()

    button = ttk.Button(root, text = 'b1: click me!', command = button1_clicked)
    button.pack()

    #button2 can be defined outside this scope since it uses lambda
    button2 = ttk.Button(root, text = 'b2: no click me!', command = lambda: button2_clicked(root)).pack()

    root.mainloop()

def button2_clicked(root):
    message = ttk.Label(root, text='Button2 was clicked!!').pack()


if __name__ == '__main__': main()