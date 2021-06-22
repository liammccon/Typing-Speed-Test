import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

def main():
    root = tk.Tk()
    center_the_screen(root, 600 ,400)

    message = ttk.Label(root, text = 'Hello, world!')
    message.pack()

    root.mainloop()

if __name__ == '__main__': main()