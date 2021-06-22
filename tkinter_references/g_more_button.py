import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from b_change_center_window import *

#syntax: button = ttk.Button(container, **option)
    #typical button: button = ttk.Button(container, text, command)

def main():
    root = tk.Tk()
    root.title('Button galore')
    center_the_screen(root, 600 ,400)

    exit_button = ttk.Button(
        root,
        text='Exit',
        command=lambda: root.quit()
    ).pack(ipadx='30', ipady='10')

    button = ttk.Button(root, text = 'Disable the button',
                        padding = '15',
                        command = lambda: disable_button(button))

    button.pack(ipadx = '10', ipady = '10', expand = True)

    # download button
    def download_clicked():
        showinfo(
            title='Information',
            message='za button clicked!'
        )
    download_icon = tk.PhotoImage(file='assets/pizza_png.png')
    download_button = ttk.Button(
        root,
        image=download_icon,
        text = 'pizza',
        compound = 'top',
        command=download_clicked
    )
    download_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )


    root.mainloop()

def disable_button(button):
    button['text'] = 'im disabled!'
    button.state(['disabled'])
    #undisable: button.state(['!disabled'])

if __name__ == '__main__': main()