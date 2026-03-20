import tkinter as tk
from tkinter import messagebox

# Function to calculate interest
def calculate():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest
        ci = p * ((1 + r/100) ** t) - p

        si_result.config(text=f"Simple Interest: {si:.2f}")
        ci_result.config(text=f"Compound Interest: {ci:.2f}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create window
root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("400x400")
root.configure(bg="#f0f8ff")

# Title
title_label = tk.Label(root, text="Interest Calculator", font=("Arial", 16, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

# Frame for inputs
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

# Principal
tk.Label(frame, text="Principal:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
principal_entry = tk.Entry(frame)
principal_entry.grid(row=0, column=1)

# Time
tk.Label(frame, text="Time (years):", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(frame)
time_entry.grid(row=1, column=1)

# Rate
tk.Label(frame, text="Rate (%):", bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=5)
rate_entry = tk.Entry(frame)
rate_entry.grid(row=2, column=1)

# Button
calc_btn = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white")
calc_btn.pack(pady=15)

# Results
si_result = tk.Label(root, text="Simple Interest: ", font=("Arial", 12), bg="#f0f8ff")
si_result.pack()

ci_result = tk.Label(root, text="Compound Interest: ", font=("Arial", 12), bg="#f0f8ff")
ci_result.pack()

# Run app
root.mainloop()