import tkinter as tk
from tkinter import ttk
from file_help_typing_test import *

#TODO make the helper .py thing a class and use its object here!

#USING OOP!
def button_pressed(textbox):
    textbox.config(state=tk.NORMAL)
    textbox.delete("1.0", tk.END)
    textbox.insert("1.0", " ")
    textbox.focus()


def return_pressed(text, textbox):
    print(text)
    textbox.config(state=tk.DISABLED)



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

        self.random_string_from_text, self.text_title = random_phrase_and_title('filtered_file.txt')

        self.create_widgets()

    def create_widgets(self):
        #Label
        text_to_type = ttk.Label(self,
                                 text=self.random_string_from_text + "\n\n~" + self.text_title,
                                 anchor=tk.CENTER, background='grey',
                                 foreground='black', wraplength = 500, justify = tk.CENTER)

        text_to_type.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW, padx=15,
                          pady=10)  # ipadx is internal to cell, padx is external
        #Text, heres good info: https://www.tutorialspoint.com/python/tk_text.htm
        textbox = tk.Text(self, height=1,
                          wrap=tk.WORD)  # height = 1 gotten from https://stackoverflow.com/questions/11464608/tkinter-text-widget-distorting-column-sizes
        textbox.insert("1.0", " ")
        textbox.bind('<Return>', lambda event: return_pressed(textbox.get("1.0", tk.END), textbox))
        textbox.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW, padx=15, pady=10)
        textbox.focus()
        #Button
        button = ttk.Button(self, text="Clear text", command = lambda: button_pressed(textbox))
        button.grid(column=0, row=2, columnspan=2, sticky='EW', padx=15, pady=10)


def center_the_screen(root, window_width = 600, window_height = 400, resizable = True):
    # get screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # get the left and top paddings
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)

    # set the positions
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    if not resizable:
        root.resizable(False, False)


def main():
    make_phrase(300, 350)
    app = App()
    app.mainloop()

if __name__ == '__main__': main()