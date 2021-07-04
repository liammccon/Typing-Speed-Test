#https://www.pythontutorial.net/tkinter/tkinter-event-binding/
import tkinter as tk
import time
from tkinter import ttk
from b_change_center_window import *

#Here i do multiple event binding on same widget with parameters

class Timer:
    def __init__(self):
        self._t1 = None
        self._t2 = None

    def t1(self, t1 = None):
        if t1:
            self._t1 = t1
        return self._t1

    def t2(self, t2 = None):
        if t2:
            self._t2 = t2
        return self._t2

    def get_time(self):
        if self._t1 and self._t2:
            return self._t2 - self._t1
        else: raise TypeError

    def get_nice_time(self):
        return '%.2f' % self.get_time()

def main():
    def start_time(event, t):
        t.t1(time.time())

    def released(event, t, message):
        t.t2(time.time())
        display_time(t, message)

    def display_time(t, message):
        message['text'] = f'You held on for {t.get_nice_time()} seconds!'
        message.pack()

    root = tk.Tk()
    center_the_screen(root, 600 ,400)

    timer = Timer()
    message = ttk.Label(root, text = '')
    button = ttk.Button(root, text = 'Press and hold ;)')
    button.bind('<Button>', lambda event: start_time(event, timer))
    button.bind('<x>', lambda event: released(event, timer, message), add = '+')
    button.focus()
    button.pack(expand = True)

    root.mainloop()

if __name__ == '__main__': main()