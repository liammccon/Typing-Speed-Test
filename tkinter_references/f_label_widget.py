import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

#BASIC LABEL: label = ttk.Label(container, **options)

def main():
    root = tk.Tk()
    center_the_screen(root, 600, 400)

    label = ttk.Label(root,
                      text = 'Hello, world!',
                      font = ('Helvetica', 15),
                      foreground = '#C74634'
                      #background = '#FFF' doesnt do anything!
                      )

    label.pack(ipadx =10, ipady = 10)

    pic = tk.PhotoImage(file = 'assets/pizza_png.png')
    image_label = ttk.Label(root,
                            image = pic,
                            text = 'Pizzaa',
                            compound = 'right',
                            padding = '40')
    image_label.pack()

    root.mainloop()

if __name__ == '__main__': main()