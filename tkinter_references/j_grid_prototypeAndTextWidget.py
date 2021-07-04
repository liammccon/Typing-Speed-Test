#https://www.pythontutorial.net/tkinter/tkinter-grid/
#https://www.tutorialspoint.com/python/tk_text.htm
import tkinter as tk
from tkinter import ttk
from b_change_center_window import *

#USING OOP!
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        center_the_screen(self, 600, 400, False)
        self.title('Typing Test')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        #Label
        text_to_type = ttk.Label(self, text="Type this text out!", anchor=tk.CENTER, background='grey',
                                 foreground='black')
        text_to_type.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW, padx=15,
                          pady=10)  # ipadx is internal to cell, padx is external
        #Text, heres good info: https://www.tutorialspoint.com/python/tk_text.htm
        textbox = tk.Text(self, height=1,
                          wrap=tk.WORD)  # height = 1 gotten from https://stackoverflow.com/questions/11464608/tkinter-text-widget-distorting-column-sizes
        textbox.insert("1.0", " ")
        textbox.bind('<Return>', lambda event: return_pressed(event, self, textbox.get("1.0", tk.END), textbox))
        textbox.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW, padx=15, pady=10)
        textbox.focus()
        #Button
        button = ttk.Button(self, text="Clear text", command = lambda: button_pressed(self, textbox))
        button.grid(column=0, row=2, columnspan=2, sticky='EW', padx=15, pady=10)

def button_pressed(root, textbox):
    textbox.config(state=tk.NORMAL)
    textbox.delete("1.0", tk.END)
    textbox.insert("1.0", " ")
    textbox.focus()

def return_pressed(event, root, text, textbox):
    print(text)
    textbox.config(state=tk.DISABLED)

def main():
    app = App()
    app.mainloop()


def SITE_STUFF(root):
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    # username
    username_label = ttk.Label(root, text="Username:")
    username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    username_entry = ttk.Entry(root)
    username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

    # password
    password_label = ttk.Label(root, text="Password:")
    password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    password_entry = ttk.Entry(root, show="*")
    password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

    # login button
    login_button = ttk.Button(root, text="Login")
    login_button.grid(column=0, row=2, columnspan=3, sticky=tk.EW, padx=5, pady=5)

if __name__ == '__main__': main()