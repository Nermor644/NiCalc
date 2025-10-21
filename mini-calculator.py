import tkinter as tk

# Functions
def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Main window
root = tk.Tk()
root.title("Mini Calculator 🧮")
root.geometry("300x400")

expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(root, width=300, height=50)
input_frame.pack(side=tk.TOP)
input_field = tk.Entry(input_frame, textvar=input_text, font=('Arial', 18), bd=5, relief=tk.RIDGE, justify='right')
input_field.pack(expand=True, fill='both')

# Buttons
btns_frame = tk.Frame(root)
btns_frame.pack(expand=True, fill='both')

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i in range(4):
    for j in range(4):
        btn_text = buttons[i][j]
        btn = tk.Button(btns_frame, text=btn_text, font=('Arial', 18), bd=2, relief=tk.RIDGE)
        btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        if btn_text == 'C':
            btn.config(command=clear)
        elif btn_text == '=':
            btn.config(command=calculate)
        else:
            btn.bind("<Button-1>", click)

# Configure grid
for i in range(4):
    btns_frame.rowconfigure(i, weight=1)
    btns_frame.columnconfigure(i, weight=1)

root.mainloop()
