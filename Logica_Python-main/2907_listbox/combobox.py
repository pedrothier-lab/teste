import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def selecao_mudou(evento):
    label.config(text=f"{evento.widget.get()}selecionado!")

combobox = ttk.Combobox(root, values=["primeiro", "Segundo", "terceiro"])

combobox.set("Primeiro")

combobox.bind("<<comboboxSelected>>",selecao_mudou)

combobox.pack()

label = tk.Label(root, text="primeiro selecionado!")
label.pack()
root.mainloop()