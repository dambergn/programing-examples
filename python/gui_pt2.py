#!/usr/bin/python3

# Windows install
# pip install tk

# Linux Install
# sudo apt-get install python3-tk -y

# https://docs.python.org/3/library/tkinter.html
# https://www.youtube.com/watch?v=ibf5cx221hk
# https://www.youtube.com/watch?v=5qOnzF7RsNA

# import sys
# if sys.version_info[0] != 3:
#     print("Please run as python3")
#     exit

import tkinter as tk
from tkinter import messagebox

class  MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Second GUI")

        self.width=800
        self.height=500
        self.geometry =str(self.width) + "x" + str(self.height)
        self.root.geometry(self.geometry)
        # self.root.geometry("800x900")

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        # print(event)
        # print(event.keysym)
        # print(event.state)
        # print("-----")
        # The above helps determin key presses for if statement
        if event.state == 12 and event.keysym == "Return":
            self.show_message

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy() #This will close the window

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()