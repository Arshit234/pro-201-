import tkinter as tk
from tkinter import ttk

def calculate_simple_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        simple_interest = (principal * rate * time) / 100
        result_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Setting up the main window
root = tk.Tk()
root.title("Simple Interest Calculator")

# Creating and placing widgets
ttk.Label(root, text="Principal:").grid(column=0, row=0, padx=10, pady=5)
principal_entry = ttk.Entry(root)
principal_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Rate of Interest (%):").grid(column=0, row=1, padx=10, pady=5)
rate_entry = ttk.Entry(root)
rate_entry.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Time (years):").grid(column=0, row=2, padx=10, pady=5)
time_entry = ttk.Entry(root)
time_entry.grid(column=1, row=2, padx=10, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_simple_interest)
calculate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="Simple Interest: ")
result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=5)

# Running the application
root.mainloop()
