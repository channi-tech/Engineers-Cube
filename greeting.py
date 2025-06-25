import tkinter as tk
from tkinter import simpledialog, messagebox
import time
root = tk.Tk()
root.withdraw()
name = simpledialog.askstring("Input", "What's your name?")
if name:
    messagebox.showinfo("Greetings",f"Hello{name}, welcome back!")
else:
        messagebox.showinfo("Greetings", "you didn't tell me your name!")
        time.sleep(5)
        root.destroy()
