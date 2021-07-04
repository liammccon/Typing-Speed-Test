import tkinter as tk


def main():
    root = tk.Tk()
    #root.geometry('WidthxHeight+-leftpadding+-rightpadding')
    #root.geometry('400x300+50+70') #400pixels wide, 300 pixels tall, 50 from left, 70 from top

    root.title('Centered Window')
    # get_title = root.title()

    center_the_screen(root)
    size_of_window = root.geometry
    if True: turn_off_resizing(root)
    else: set_min_max_resize(root) #not working

    root.attributes('-alpha', .9)#transparence
    root.attributes('-topmost', 1) #always on top (can change, look https://www.pythontutorial.net/tkinter/tkinter-window/)
    root.iconbitmap('./keyboard-icon.icns') #SHOULD WORK :(

    root.mainloop()

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

def turn_off_resizing(root):
    root.resizable(False, False)

def set_min_max_resize(root):
    root.resizable(True, True)
    #NOT WORKING! https://www.pythontutorial.net/tkinter/tkinter-window/
    print("THIS ISNT WORKING")
    min_width, min_height, max_width, max_height = 500, 300, 700, 500
    root.minsize(min_width, min_height)
    root.maxsize(max_height, max_height)

if __name__ == '__main__': main()