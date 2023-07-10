import tkinter as tk
from tkinter import messagebox
from tkinter import Label


window = tk.Tk()
window.geometry("800x400")

# add label to the root window
label1 = Label(window, text="New user?")
label1.pack()


def login_callback():
    # messagebox.showinfo("Hello Python", "Hello World")
    label1.configure(text="Welcome")


hello_button = tk.Button(window, text="Login", bg="red", command=login_callback)
hello_button.pack(side=tk.LEFT)


window.mainloop()
