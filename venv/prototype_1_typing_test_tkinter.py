import time
import tkinter as tk
from tkinter import ttk
from file_help_typing_test import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Typing Test')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        #self.rowconfigure(2, weight=1)

        self.random_string_from_text, self.text_title = None, None
        self.before_start = True
        self.finished = False
        self.t1, self.t2 = None, None

        self.before_start_text = "Press 'Enter' to start the typing test, and press 'Enter' again when you finished typing"
        self.before_start_wraplength = 300

        #Label
        self.text_to_type = ttk.Label(self, anchor=tk.CENTER, background='grey',
                                      foreground='black',
                                      justify=tk.CENTER)

        #Text
        self.textbox = tk.Text(self, height=1,
                               wrap=tk.WORD)  # height = 1 gotten from https://stackoverflow.com/questions/11464608/tkinter-text-widget-distorting-column-sizes
        center_the_screen(self, 600, 400, False)

        self.set_grid()
        self.set_before_start()

    def set_grid(self):
        #Label
        self.text_to_type.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW, padx=15,
                          pady=10)  # ipadx is internal to cell, padx is external
        self.text_to_type.bind('<Return>', lambda event: self.return_pressed())
        self.text_to_type.focus()

        #Text, heres good info: https://www.tutorialspoint.com/python/tk_text.htm
        self.textbox.bind('<Return>', lambda event: self.return_pressed())
        self.textbox.bind('<KeyRelease-Return>', lambda event: self.return_released())
        self.textbox.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW, padx=15, pady=20)

    def set_before_start(self):
        #Set the widgets to their state before the user starts the typing test
        self.before_start = True
        self.finished = False
        self.text_to_type.config(text=self.before_start_text, wraplength=self.before_start_wraplength)
        self.text_to_type.focus()

        self.textbox.config(state=tk.NORMAL)
        self.textbox.delete("1.0", tk.END) #BUG
        self.textbox.config(state = tk.DISABLED)

        self.get_random_string()

    def set_during_test(self):
        #Set widgets to their state during the typing test
        self.before_start = False
        self.finished = False
        self.text_to_type.config(wraplength=500, text=self.random_string_from_text + "\n\n~" + self.text_title)
        self.textbox.config(state=tk.NORMAL)
        self.textbox.focus()
        self.t1 = time.time()

    def set_finished(self):
        #Set widgets to their state after the typing test
        self.before_start = False
        self.finished = True
        self.t2 = time.time()
        user_text = self.textbox.get("1.0", tk.END)
        accuracy_float = compare_char_sequence(self.random_string_from_text, user_text)
        user_words = string_to_word_char_list(user_text)
        words_per_min = ((len(user_words) / (self.t2 - self.t1)) * 60)  # NEED TO ADD TIMER SOMEWHERE
        score = get_score(words_per_min, accuracy_float)
        a = f'Words per minute: %.2f\n' % words_per_min
        b = f'Accuracy: %.0f percent\n' % (accuracy_float * 100)
        c = f'Your score: %.0f\n' % score
        d = '------------------------\n'
        e = "Press 'Enter' to try again\n"
        display = a + b + c + d + e
        self.text_to_type.config(text=display)
        self.textbox.config(state=tk.DISABLED)
        self.finished = True

    def return_pressed(self):
        if self.before_start:
            self.set_during_test()
        if self.finished:
            self.set_before_start()
        else:
            if len(self.textbox.get("1.0", tk.END))>1 and not self.finished:
                self.set_finished()

    def return_released(self):
        #Protects against user pressing enter when nothing has been entered
        if not self.before_start or not self.finished:
            if len(self.textbox.get("1.0", tk.END)) <= 2:
                self.textbox.delete("1.0", tk.END)

    def button_pressed(self):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.delete("1.0", tk.END)
        self.textbox.focus()
        if self.finished:
            self.set_before_start()

    def get_random_string(self):
        self.random_string_from_text, self.text_title = random_phrase_and_title('filtered_file.txt')

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
    make_phrase(200, 250)
    app = App()
    app.mainloop()

if __name__ == '__main__': main()