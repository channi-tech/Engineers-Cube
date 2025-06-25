import tkinter as tk
window = tk.Tk()
window.title("calculator")
window.geometry("300x400")
display = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
def button_click(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(item))
def button_clear():
    display.delete(0, tk.END)
def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]
button_frame = tk.Frame(window)
button_frame.pack()
for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == "=":
          btn = tk.Button(button_row, text=btn_text, font=("Arial", 18), fg="white", bg="green", command=button_equal)
        elif btn_text == "C":
            btn = tk.Button(button_row, text=btn_text, font=("Arial", 18), fg="white", bg="red", command=button_clear)
        else:
            btn = tk.Button(button_row, text=btn_text, font=("Arial", 18), command=lambda txt=btn_text: button_click(txt))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
window.mainloop()                            








            
            
    
