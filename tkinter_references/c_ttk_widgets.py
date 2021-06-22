#https://www.pythontutorial.net/tkinter/tkinter-ttk/import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

def main():
    root = tk.Tk()
    center_the_screen(root) #from b

    #classic_vs_styled(root)

    three_ways_to_set_widget(root)

    root.mainloop()

def classic_vs_styled(root):
    tk.Label(root, text='Classic Label').pack()
    ttk.Label(root, text='Themed Label').pack()  # USE TTK NOT TK! Theyre better :)

def three_ways_to_set_widget(root):
    #https://www.pythontutorial.net/tkinter/tkinter-options/
    #1: with kwargs
    ttk.Label(root, text='Widget configured w kwargs').pack()

    #2:use dictionary index after creation
    label = ttk.Label(root)
    label['text'] = 'Widget configured w index after creation'
    label.pack()

    #3 with config() and kwargs
    label2 = ttk.Label(root)
    label2.config(text = 'Widgett configured with config()')
    label2.pack()


if __name__ == '__main__': main()