import OOP_project as oop
import tkinter as tk

root = tk.Tk()
root.title("Lifechoices Progress Calculator")
root.geometry("800x500")

myCanvas = tk.Canvas(root, bg="white", height=500, width =800 )

section = tk.Label(root, bg="green", height=10, width=10)
section.config(font=('helvetica', 10))
myCanvas.create_window(20, 10, window=section)
myCanvas.pack()

root.mainloop()