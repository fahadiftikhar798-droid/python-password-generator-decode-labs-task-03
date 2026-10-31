import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password():
    length = int(length_var.get())
    chars = ""
    if upper_var.get(): chars += string.ascii_uppercase
    if lower_var.get(): chars += string.ascii_lowercase
    if digits_var.get(): chars += string.digits
    if symbols_var.get(): chars += string.punctuation
    
    if not chars:
        password_var.set("Select at least one option!")
        return
    
    pwd = "".join(random.choice(chars) for _ in range(length))
    password_var.set(pwd)
    
    # Strength
    if length < 8: strength_label.config(text="Weak", foreground="red")
    elif length < 12: strength_label.config(text="Medium", foreground="orange")
    else: strength_label.config(text="Strong", foreground="green")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x450")

password_var = tk.StringVar(value="xT9@kL2$pQ7!")
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold")).pack(pady=15)
ttk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25).pack(pady=10)
ttk.Button(root, text="Copy", command=copy_password).pack()

ttk.Label(root, text="Password Length").pack()
ttk.Scale(root, from_=4, to=32, variable=length_var, orient="horizontal").pack(fill="x", padx=20)

ttk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Include Lowercase", variable=lower_var).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Include Numbers", variable=digits_var).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=20)

strength_label = ttk.Label(root, text="Strong")
strength_label.pack(pady=10)

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=20, ipadx=20, ipady=10)

root.mainloop()