import tkinter as tk
from tkinter import ttk
import os
import sys
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x550")  
janela.resizable(False, False)

pasta_do_script = os.path.dirname(os.path.abspath(sys.argv[0]))


nome_imagem = "imagem.jfif"
caminho_imagem = os.path.join(pasta_do_script, nome_imagem)

try:
    img_original = Image.open(caminho_imagem)

    img_redimensionada = img_original.resize((120, 120), Image.Resampling.LANCZOS)
    
    imagem_avatar = ImageTk.PhotoImage(img_redimensionada)

except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

    imagem_avatar = None

titulo = tk.Label(
    janela,
    text="Faça seu Login",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

if imagem_avatar:
    lbl_imagem = tk.Label(janela, image=imagem_avatar)
    lbl_imagem.pack(pady=10)
else:
    lbl_imagem = tk.Label(janela, text="[Erro na Imagem]", fg="red")
    lbl_imagem.pack(pady=10)

lbl_usuario = tk.Label(janela, text="Usuário")
lbl_usuario.pack(anchor="w", padx=50)

entry_usuario = ttk.Entry(janela, width=35)
entry_usuario.pack(padx=50, pady=(0, 10), fill="x")

lbl_senha = tk.Label(janela, text="Senha")
lbl_senha.pack(anchor="w", padx=50)

entry_senha = ttk.Entry(janela, width=35, show="*")
entry_senha.pack(padx=50, pady=(0, 10), fill="x")

lembrar = tk.BooleanVar()

check = ttk.Checkbutton(
    janela,
    text="Lembrar-me",
    variable=lembrar
)
check.pack(anchor="w", padx=50, pady=(5, 5))

botao = ttk.Button(
    janela,
    text="Entrar"
)
botao.pack(fill="x", padx=50, pady=15)

esqueceu = tk.Label(
    janela,
    text="Esqueceu a senha?",
    fg="blue",
    cursor="hand2",
    font=("Arial", 10, "underline")
)
esqueceu.pack(pady=10)

janela.mainloop()
