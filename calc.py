import tkinter as tk
from tkinter import messagebox

# Function to update the expression
def update_expression(symbol):
    current_text = expression_var.get()
    expression_var.set(current_text + str(symbol))

# Function to clear the expression
def clear_expression():
    expression_var.set("")

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression_var.get())
        expression_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        expression_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the window size
root.geometry("400x600")

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create and place the display
expression_var = tk.StringVar()
display = tk.Entry(root, textvariable=expression_var, font=("Helvetica", 24), bd=10, insertwidth=4, width=14, borderwidth=4, bg="lightgrey")
display.grid(row=0, column=0, columnspan=4)

# Create button text and colors
button_texts = [
    ('7', 'lightblue'), ('8', 'lightblue'), ('9', 'lightblue'), ('/', 'orange'),
    ('4', 'lightblue'), ('5', 'lightblue'), ('6', 'lightblue'), ('*', 'orange'),
    ('1', 'lightblue'), ('2', 'lightblue'), ('3', 'lightblue'), ('-', 'orange'),
    ('0', 'lightblue'), ('C', 'red'), ('=', 'green'), ('+', 'orange')
]

# Function to create and place buttons
def create_button(symbol, color, row, col):
    button = tk.Button(root, text=symbol, padx=20, pady=20, font=("Helvetica", 18), bg=color,
                       command=lambda: update_expression(symbol) if symbol not in ["C", "="] else (clear_expression() if symbol == "C" else evaluate_expression()))
    button.grid(row=row, column=col, sticky="nsew")

# Place buttons in a grid
row_val, col_val = 1, 0
for (text, color) in button_texts:
    create_button(text, color, row_val, col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure row and column weights for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()