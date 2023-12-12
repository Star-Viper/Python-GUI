import tkinter as tk
import math

def calculate_factorial():
    try:
        num = int(entry.get())
        result_text.set(f"Factorial of given number is : {math.factorial(num)}")
    except ValueError:
        result_text.set("Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Factorial Calculator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Enter a number:").grid(row=0, column=0)
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

calculate_button = tk.Button(frame, text="Calculate Factorial", command=calculate_factorial)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text)
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
