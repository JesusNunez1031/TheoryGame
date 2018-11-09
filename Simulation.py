from tkinter import messagebox

#import PIL.Image, PIL.ImageTk
#import numpy as np
import tkinter
from tkinter import *
#import cv2


def showDFA():
    # Create a window
    window = tkinter.Toplevel()
    window.title('Figure Out the DFA')

    # Load the image using opencv
    cv_img = cv2.cvtColor(cv2.imread('DFA_Test.png'), cv2.COLOR_BGR2RGB)

    # Get the image dimensions(OpenCV stores image data as NumPy ndarray)
    height, width, no_channels = cv_img.shape

    # Create a canvas that can fit the above image
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack()

    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

    # Add a PhotoImage to the canvas
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    # the window closes after 10000ms(60000ms = 1min)
    window.after(10000, window.destroy)
    window.mainloop()


# showDFA()

def helpmenu():
    messagebox.showinfo("Help", "A DFA will be shown for 30s. Study the DFA shown and then "
                                "input as many string as you can. Your score will then depend on how"
                                " many strings are accepted by the DFA. ")


def About():
    messagebox.showinfo("About", "This is our theory of computation project")


def Strings():
    Strlist = []
    for i in range(5):
        x = str(input("Enter strings. \n"))
        Strlist.insert(i, x)
        i += 1
    print(list)


# Strings()


def MainWindow():
    main = tkinter.Tk()
    main.title('Main Menu')
    menu = Menu(main)

    # create a toplevel menu
    main.config(menu=menu)
    filemenu = Menu(menu)

    menu.add_cascade(label="Game", menu=filemenu)
    filemenu.add_command(label='Play', command=showDFA)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=main.destroy)

    Helpmenu = Menu(menu)
    # menu.add_cascade(label="Help", menu=filemenu)
    filemenu.add_command(label="Instructions", command=helpmenu)
    filemenu.add_command(label="About...", command=About)

    main.geometry("400x300")
    main.mainloop()

MainWindow()

# class MainWindow(Frame):
#
#     def __init__(self, master=None):
#         # parameters that you want to send through the Frame class.
#         Frame.__init__(self, master)
#
#         # reference to the master widget, which is the tk window
#         self.master = master
#
#         # with that, we want to then run init_window, which doesn't yet exist
#         self.init_window()
#
#     # Creation of init_window
#     def init_window(self):
#         # changing the title of our master widget
#         self.master.title("Main Menu")
#
#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)
#
#         # creating a menu instance
#         menu = Menu(self.master)
#         self.master.config(menu=menu)
#
#         # create the file object)
#         file = Menu(menu)
#
#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         file.add_command(label="Exit", command=self.client_exit)
#
#         # added "Game" to our menu
#         menu.add_cascade(label="Game", menu=file)
#
#         # create the file object)
#         edit = Menu(menu)
#
#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         edit.add_command(label="Undo")
#
#         # added "file" to our menu
#         menu.add_cascade(label="Edit", menu=edit)
#
#     def client_exit(self):
#         exit()
#
#
# # root window created. Here, that would be the only window, but
# # you can later have windows within windows.
# root = Tk()
#
# root.geometry("400x300")
#
# # creation of an instance
# app = MainWindow(root)
#
# # mainloop
# root.mainloop()
