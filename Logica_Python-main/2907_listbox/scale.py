import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Senai - sistemas")
root.geometry("800x600")

def valor_mudou(evento):
    label.config(text=evento)

scale = tk.Scale(root,
    from_=0,
    to=10,
    orient="horizontal",
    command=valor_mudou)
scale.pack()

label = tk.Label(root, text="0")
label.pack()

root.mainloop()
# Controle na horizotal

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Senai - sistemas")
root.geometry("800x600")

def valor_mudou(evento):
    label.config(text=evento)

scale = tk.Scale(root,
    from_=0,
    to=10,
    orient="vertical",
    command=valor_mudou)
scale.pack()

label = tk.label(root, text="0")
label.pack()

root.mainloop()
# controle na vertical