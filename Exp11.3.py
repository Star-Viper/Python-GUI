import tkinter as tk

root = tk.Tk()
root.title("Christmas Tree")

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

canvas.create_polygon(50, 300, 200, 50, 350, 300, fill='green')

canvas.create_rectangle(170, 300, 230, 350, fill='brown')

canvas.create_oval(150, 150, 180, 180, fill='red')
canvas.create_oval(210, 210, 220, 220, fill='red')
canvas.create_oval(250, 250, 280, 280, fill='red')

root.mainloop()
