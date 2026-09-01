import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def enter_pressionado(event):
    label.config(text=event.widget.get())

entry = tk.Entry(root)
entry.insert(0, "digite seu texto")
entry.bind("<Return>", enter_pressionado)
entry.pack()

label = tk.Label(root, text="demonstração!")
label.pack()
root.mainloop()
