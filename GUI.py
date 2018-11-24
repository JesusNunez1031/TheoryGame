import tkinter as tk

LARGE_FONT = ("Monaco", 24)

class GUI(tk.Tk):
    # args - pass any arguments
    # kwargs - keyword arguments
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # first paramter is the minimum size, weight is the priority,
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        #nsew, north south east west stretches the window to be uniform
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # makes this frame pops up
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # parent would be GUI (main class)
        label = tk.Label(self, text="GAME MENU", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

application = GUI()
application.mainloop()