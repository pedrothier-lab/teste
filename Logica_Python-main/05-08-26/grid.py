import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")

for linha in range(3):
    for coluna in range(3):
        tk.Button(
            root,
            text=f"cell ({linha}, {coluna})",
            width=20,
            height=5,
        ).grid(row=linha, column=coluna, padx=2, pady=2)
tk.Button(
    root,
    text="Span 2 coluns",
    height=5,
).grid(row=3, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

tk.Button(
    root,
    text="Span 2 rows",
    width=20,
    height=10,
).grid(row=4, column=0, columnspan=2, sticky="ns", padx=2, pady=2)

root.mainloop()
