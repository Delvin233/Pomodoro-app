import time  # just for a timer
import threading  # to enable us interract with thE UI
import tkinter as tk  # gui library
from tkinter.ttk import *
from tkinter import ttk, PhotoImage


# we would use a class (OOP) :)
class Pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")  # size of the window
        self.root.title("Pomodoro Timer")  # title obviously
        self.root.tk.call(
            "wm", "iconphoto", self.root._w, PhotoImage(file="images/tomato.png")
        )

        # styling the gui
        self.s = ttk.Style()
        self.s.configure(
            "TNotebook.Tab", font=("Callibri", 16)
        )  # the tabs are basically the sections for the pomodoro app
        self.s.configure("TButton", font=("Callibri", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=20, padx=50, expand=True)

        #  placing a frame or a wrap around the tab
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        # adding a name to the tab
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        # creating label for the individual tabs
        self.pomo_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 50))
        self.pomo_timer_label.pack(pady=20)

        self.short_break_label = ttk.Label(self.tab2, text="5:00", font=("Ubuntu", 50))
        self.short_break_label.pack(pady=20)

        self.short_break_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 50))
        self.short_break_label.pack(pady=20)

        # Buttons for start , skip and reset
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(
            self.grid_layout, text="Start", command=self.start_timer
        )
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(
            self.grid_layout, text="Skip", command=self.skip_timer
        )
        self.skip_button.grid(row=0, column=1)

        self.rset_button = ttk.Button(
            self.grid_layout, text="Reset", command=self.reset_timer
        )
        self.rset_button.grid(row=0, column=2)

        # Pomodoro's counter
        self.pomo_counter = ttk.Label(
            self.grid_layout, text="Pomodoro's Count : 0", font="Ubuntu"
        )
        self.pomo_counter.grid(row=1, column=0, columnspan=3, pady=10)

        # loop to keep the app running
        self.root.mainloop()

        # functions to control the start, skip, reset and pomodoro counter

        # initial parameters to work with
        self.pomos_done = 0
        self.skipped = False
        self.stopped = False

    def start_timer_thread(self):
        pass

    def start_timer(self):
        pass

    def reset_timer(self):
        pass

    def skip_timer(self):
        pass


# calling the class
Pomodoro()
