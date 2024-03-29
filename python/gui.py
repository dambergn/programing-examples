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

root = tk.Tk()

width=800
height=500
geometry =str(width) + "x" + str(height)

root.geometry(geometry)
root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

myentry = tk.Entry(root)
myentry.pack(padx=10)

def buttonClick():
    print("Button Clicked!")

button = tk.Button(root, text="Click Me!", font=('Arial, 18'), command=buttonClick)
button.pack(padx=10, pady=10)


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn2.grid(row=0, column=2, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn2.grid(row=1, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn2.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=width/2-50, y=350, height=100, width=100)

root.mainloop()