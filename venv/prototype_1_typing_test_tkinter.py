import time
import tkinter as tk
from tkinter import ttk
from file_help_typing_test import *

#ISSUES
#-trying to delete the return press doesnt work because it deletes before return is processed.
#-if you press return on empty box itll still show the return

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Typing Test')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=1)

        self.random_string_from_text, self.text_title = None, None
        self.get_random_string()

        self.before_start = True
        self.finished = False
        self.t1, self.t2 = None, None

        self.before_start_text = "Press 'Enter' to start the typing test, and press 'Enter' again when you finished typing"
        self.before_start_wraplength = 300
        self.text_to_type = ttk.Label(self, text = self.before_start_text,
                                      anchor=tk.CENTER, background='grey',
                                      foreground='black',
                                      wraplength = self.before_start_wraplength,
                                      justify=tk.CENTER)


        self.button = ttk.Button(self, text="Clear text", command=lambda: self.button_pressed())
        self.textbox = tk.Text(self, height=1, state=tk.DISABLED,
                               wrap=tk.WORD)  # height = 1 gotten from https://stackoverflow.com/questions/11464608/tkinter-text-widget-distorting-column-sizes
        center_the_screen(self, 600, 400, False)

        self.set_grid()

    def get_random_string(self):
        self.random_string_from_text, self.text_title = random_phrase_and_title('filtered_file.txt')

    def set_grid(self):
        #Label
        self.text_to_type.grid(column=0, row=0, columnspan=2, sticky=tk.NSEW, padx=15,
                          pady=10)  # ipadx is internal to cell, padx is external
        self.text_to_type.bind('<Return>', lambda event: self.return_pressed())
        self.text_to_type.focus()

        #Text, heres good info: https://www.tutorialspoint.com/python/tk_text.htm
        self.textbox.insert("1.0", " ")
        self.textbox.bind('<Return>', lambda event: self.return_pressed(self.textbox.get("1.0", tk.END), self.textbox, self.random_string_from_text))
        self.textbox.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW, padx=15, pady=10)

        #Button
        self.button.grid(column=0, row=2, columnspan=2, sticky='EW', padx=15, pady=10)

    def return_pressed(self, text = None, textbox = None, string_from_text = None):
        if self.before_start:
            self.text_to_type.config(wraplength = 500, text=self.random_string_from_text + "\n\n~" + self.text_title)
            self.textbox.config(state=tk.NORMAL)
            self.textbox.focus()
            self.before_start = False
            self.t1 = time.time()
        else:
            if len(text)>1 and not self.finished:#NOT WORKING (if you just press enter at beg)
                self.t2 = time.time()
                print(text)
                # TODO
                accuracy_float = compare_char_sequence(string_from_text, text)
                user_words = string_to_word_char_list(text)
                words_per_min = ((len(user_words) / (self.t2 - self.t1)) * 60)  # NEED TO ADD TIMER SOMEWHERE
                score = get_score(words_per_min, accuracy_float)
                a = f'Words per minute: %.2f\n' % words_per_min
                b = f'Accuracy: %.0f percent\n' % (accuracy_float * 100)
                c= f'Your score: %.0f\n' % score
                display = a + b + c
                self.text_to_type.config(text = display)
                print(f'Words per minute: %.2f ' % words_per_min)
                print(f'Accuracy: %.0f percent' % (accuracy_float * 100))
                print('Your score: %.0f' % score)
                #
                textbox.config(state=tk.DISABLED)
                self.finished=True
                self.button.config(text="Try again?")
            else: #text length is empty
                self.textbox.config(state=tk.NORMAL)
                self.textbox.delete("1.0", tk.END) #NOT WORKING
                self.textbox.focus()
                print("HI")

    def button_pressed(self):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.delete("1.0", tk.END)
        self.textbox.focus()
        if self.finished:
            self.before_start=True
            self.finished=False
            self.text_to_type.config(text = self.before_start_text, wraplength = self.before_start_wraplength)
            self.text_to_type.focus()
            self.get_random_string()
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