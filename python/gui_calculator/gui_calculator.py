#!/usr/bin/python3

# Windows install
# pip install tk

# Linux Install
# sudo apt-get install python3-tk -y

# https://docs.python.org/3/library/tkinter.html
# https://www.youtube.com/watch?v=ibf5cx221hk

# import sys
# if sys.version_info[0] != 3:
#     print("Please run as python3")
#     exit

import tkinter as tk
from tkinter import messagebox

class  MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

MyGUI()