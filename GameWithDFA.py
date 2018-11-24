from tkinter import messagebox

from termcolor import colored

import PIL.Image, PIL.ImageTk
import time
import tkinter
from tkinter import *
import cv2
import copy

Set = set()


# This machine will accept a string and check if there is a connective
def machine_accepts_characters_with_consecutive(userInput):
    if (type(userInput) != str):
        raise TypeError("Value is not a string")
    states = [0 for i in range(
        5)]  # Size of array represents the number of states, right now we will make my_array[4] the accept state
    states[0] = 1
    count = 0
    for i in range(len(userInput)):
        if count == 4:
            # Count won't increment because the string has fit the criteria
            count = 4
        elif (ord(userInput[i]) < ord("d") and ord(userInput[i]) > ord("a") - 1):
            count += 1
            # Now we will show animation of states[count] lighting up or something
            states[count - 1] = 0
            states[count] = 1

        else:
            # String doesn't fit criteria yet so we set count back to 0
            states[count] = 0
            count = 0
            states[count] = 1
        # print(states)
    return count == 4


def takesInput():
    validInputs = set()
    start = time.time()
    # Time is in seconds
    PERIOD_OF_TIME = 20
    print("Enter as many regular expressions as you can before the time ends: ")
    while True:
        userInput = input(colored("New String: ", "blue"))
            #.replace(" ", "")

        # this is the split of the non-spaced string format [a, d, f, t]
        #exp = list(userInput)

        #print(exp)
        if machine_accepts_characters_with_consecutive(userInput):
            Set.add(userInput)
            print(userInput + colored(" is valid", "green"))
        else:
            print(userInput + colored(" is invalid", "red"))

        if time.time() > start + PERIOD_OF_TIME: break
    print(colored("Your time is up! This is the set of correct strings you entered: ", "blue"))
    print(Set)

#################################################################################################


# exp = ['b', '*', 'a', '+', 'a']
# var_test = []
# rules_input = ["E -> E + T", "E -> T", "T -> T * F", "T -> F", "T -> F", "F -> (E)", "F -> a", "F -> b"]
# stack = []
# var = []
# final = []
# main()

takesInput()


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


def MainWindow():
    main = tkinter.Tk()
    main.title('Main Menu')
    menu = Menu(main)

    # create a toplevel menu
    main.config(menu=menu)
    filemenu = Menu(menu)

    menu.add_cascade(label="Game", menu=filemenu)
    filemenu.add_command(label='ShowDFA', command=showDFA)
    filemenu.add_command(label='Start Game', command=takesInput)
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
