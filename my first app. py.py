import tkinter as tk
window = tk.Tk()
window.title("my First App")
window.geometry("400x300")
def on_button_click():
    label.config(text="You clicked the button!")
def show_name():
    user_name = entry.get()
    label.config(text=f"hello, {user_name}! Welcome!")
label = tk.Label(window, text="Welcome to My first GUI App!" , font=("Arial" , 14))
label.pack(pady=20)
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)
button = tk.Button(window, text="Submit", font=("Arial", 12), command=show_name)
button.pack(pady=10)
window.mainloop()
