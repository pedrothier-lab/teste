import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def carregar_foto():
    caminho_imagem = r"imagem.jfif"

    if os.path.exists(caminho_imagem):
        img_original = Image.open(caminho_imagem)

        img_redimensionada = img_original.resize(
            (120, 120), Image.Resampling.LANCZOS
        )



root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("1000x600")

padx_val = 5
pady_val = 5

# lbl_foto = tk.Label(
#     root, text="[ Carregando... ]", bg="lightgray", width=130, height=130
# )
# lbl_foto.grid_propagate(False)
# lbl_foto.grid(
#     row=0, column=0, rowspan=5, padx=padx_val, pady=pady_val, sticky="nsew"
# )

foto_tkinter = ImageTk.PhotoImage(file="imagem.jfif")
lbl_foto = tk.Label(image=foto_tkinter, text="")
lbl_foto.grid(row=0, column=0, rowspan=5)

lbl_nome = tk.Label(root, text="Nome:")
lbl_nome.grid(row=0, column=1, sticky="w", padx=padx_val, pady=pady_val)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=2, sticky="ew", padx=padx_val, pady=pady_val)

lbl_genero = tk.Label(root, text="Gênero:")
lbl_genero.grid(row=1, column=1, sticky="w", padx=padx_val, pady=pady_val)
combo_genero = ttk.Combobox(
    root, values=["Masculino", "Feminino", "Não-binário", "Outro"]
)
combo_genero.grid(row=1, column=2, sticky="ew", padx=padx_val, pady=pady_val)
combo_genero.current(0)

lbl_olho = tk.Label(root, text="Cor do Olho:")
lbl_olho.grid(row=2, column=1, sticky="w", padx=padx_val, pady=pady_val)
combo_olho = ttk.Combobox(
    root, values=["Castanho", "Azul", "Verde", "Mel", "Preto", "Outra"]
)
combo_olho.grid(row=2, column=2, sticky="ew", padx=padx_val, pady=pady_val)
combo_olho.current(0)

lbl_altura = tk.Label(root, text="Altura (m):")
lbl_altura.grid(row=3, column=1, sticky="w", padx=padx_val, pady=pady_val)
entry_altura = tk.Entry(root)
entry_altura.grid(row=3, column=2, sticky="ew", padx=padx_val, pady=pady_val)

lbl_peso = tk.Label(root, text="Peso (kg):")
lbl_peso.grid(row=4, column=1, sticky="w", padx=padx_val, pady=pady_val)
entry_peso = tk.Entry(root)
entry_peso.grid(row=4, column=2, sticky="ew", padx=padx_val, pady=pady_val)

btn_enviar = tk.Button(root, text="Enviar", width=12)
btn_enviar.grid(row=5, column=2, sticky="e", padx=padx_val, pady=pady_val)

root.columnconfigure(2, weight=1)


carregar_foto()
root.mainloop()
