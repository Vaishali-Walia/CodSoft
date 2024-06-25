import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to handle the password generation and display it
def generate():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a positive number.")
            return
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")
root.configure(bg='#2e3f4f')

# Customize font
font_style = ("Helvetica", 16, "bold")
font_button = ("Helvetica", 14, "bold")

# Create and place widgets
tk.Label(root, text="Enter the desired length for the password:", font=font_style, bg='#2e3f4f', fg='white').pack(pady=30)

entry = tk.Entry(root, font=font_style, bg='#cfd8dc', fg='#37474f', width=15)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", font=font_button, bg='#00695c', fg='white', command=generate)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=font_style, bg='#2e3f4f', fg='#ffeb3b')
result_label.pack(pady=30)

# Run the application
root.mainloop()