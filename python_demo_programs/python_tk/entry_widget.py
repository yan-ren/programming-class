import tkinter as tk

window = tk.Tk()
window.geometry("800x400")

# declaring string variable for storing name and password
name = tk.StringVar()
password = tk.StringVar()

name_label = tk.Label(window, text="Username")
name_entry = tk.Entry(window, textvariable=name)

password_label = tk.Label(window, text="Password")
password_entry = tk.Entry(window, textvariable=password)


def submit():
    name_value = name.get()
    password_value = password.get()

    print("name is", name_value)
    print("password is", password_value)

    name.set("")
    password.set("")


# create submit button
sub_btn = tk.Button(window, text="Submit", command=submit)

name_label.pack()
name_entry.pack()
password_label.pack()
password_entry.pack()
sub_btn.pack()

window.mainloop()
