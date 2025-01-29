import tkinter as tk
from tkinter import messagebox
import math

def click(button_text):
    current = entry_var.get()
    entry_var.set(current + button_text)

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get(), {"__builtins__": None}, math.__dict__)
        entry_var.set(str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        entry_var.set("")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x550")
root.configure(bg="#2C3E50")
entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20, "bold"), bd=10, relief=tk.RIDGE, justify='right', fg='white', bg="#34495E")
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+'),
    ('sin', 'cos', 'tan', 'log'),
    ('asin', 'acos', 'atan', 'exp'),
    ('sqrt', 'pow', '(', ')')
]

def scientific_function(func):
    try:
        result = str(eval(f"math.{func}({entry_var.get()})"))
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Function Usage")
        entry_var.set("")

frame = tk.Frame(root, bg="#2C3E50")
frame.pack()

for row in buttons:
    button_frame = tk.Frame(frame, bg="#2C3E50")
    button_frame.pack(side=tk.TOP)
    for char in row:
        if char in ('C', '='):
            action = clear if char == 'C' else calculate
        elif char in ('sin', 'cos', 'tan', 'log', 'sqrt', 'asin', 'acos', 'atan', 'exp'):
            action = lambda x=char: scientific_function(x)
        else:
            action = lambda x=char: click(x)
        tk.Button(button_frame, text=char, font=("Arial", 18, "bold"), width=5, height=2, command=action, bg="#FADBD8", fg='black', bd=5, relief=tk.RAISED).pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()