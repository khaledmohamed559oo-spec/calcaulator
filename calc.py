import tkinter as tk

window = tk.Tk()
window.title("Calc")
window.geometry("300x400")
window.configure(bg="#d0e6f7")    
 
entry = tk.Entry(window, font=('Arial', 20), bd=5, relief=tk.RIDGE, justify='right', bg="#ffffff")
entry.pack(pady=20)
 
buttons_frame = tk.Frame(window, bg="#d0e6f7")
buttons_frame.pack()
 
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, " wrong ")
 
button_bg = "#ffffff"
button_fg = "#000000"
operation_bg = "#b22222"    
operation_fg = "#ffffff"    
 
number = 0
for row in range(3):
    for col in range(3):
        btn = tk.Button(buttons_frame, text=str(number), width=8, height=4,
                        font=('Arial', 16),
                        command=lambda num=number: entry.insert(tk.END, str(num)),
                        bg=button_bg, fg=button_fg)
        btn.grid(row=row, column=col, padx=5, pady=5)
        number += 1
 
plus_button = tk.Button(buttons_frame, text='+', width=8, height=4,
                        font=('Arial', 16),
                        command=lambda: entry.insert(tk.END, '+'),
                        bg=operation_bg, fg=operation_fg)
plus_button.grid(row=3, column=2, padx=5, pady=5)
 
equal_button = tk.Button(buttons_frame, text='=', width=8, height=4,
                         font=('Arial', 16),
                         command=calculate,
                         bg=operation_bg, fg=operation_fg)
equal_button.grid(row=3, column=1, padx=5, pady=5)
 
c_button = tk.Button(buttons_frame, text="c", width=8, height=4,
                     font=("Arial", 16),
                     command=lambda: entry.delete(0, tk.END),
                     bg=operation_bg, fg=operation_fg)
c_button.grid(row=3, column=0, padx=5, pady=5)
 
window.mainloop()
