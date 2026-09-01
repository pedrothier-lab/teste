import tkinter as tk
from tkinter import ttk

# Taxas de exemplo em relação ao Real
taxas = {
    "BRL": 1.00,
    "USD": 5.50,
    "EUR": 6.40
}


def converter():
    try:
        valor = float(entrada_valor.get().replace(",", "."))

        origem = combo_origem.get()
        destino = combo_destino.get()

    
        valor_brl = valor * taxas[origem]

       
        resultado = valor_brl / taxas[destino]

        label_resultado.config(
            text=f"{resultado:.2f} {destino}"
        )

    except ValueError:
        label_resultado.config(
            text="Digite um valor válido."
        )



janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("400x350")
janela.resizable(False, False)


titulo = tk.Label(
    janela,
    text="Conversor de Moedas",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)


label_valor = tk.Label(
    janela,
    text="Digite o valor:",
    font=("Arial", 11)
)
label_valor.pack()

entrada_valor = tk.Entry(
    janela,
    font=("Arial", 12),
    justify="center"
)
entrada_valor.pack(pady=8)


label_origem = tk.Label(
    janela,
    text="Moeda de origem:",
    font=("Arial", 11)
)
label_origem.pack()

combo_origem = ttk.Combobox(
    janela,
    values=["BRL", "USD", "EUR"],
    state="readonly",
    justify="center",
    width=20
)
combo_origem.pack(pady=8)
combo_origem.set("BRL")


label_destino = tk.Label(
    janela,
    text="Moeda de destino:",
    font=("Arial", 11)
)
label_destino.pack()

combo_destino = ttk.Combobox(
    janela,
    values=["BRL", "USD", "EUR"],
    state="readonly",
    justify="center",
    width=20
)
combo_destino.pack(pady=8)
combo_destino.set("USD")


botao_converter = tk.Button(
    janela,
    text="Converter",
    command=converter,
    font=("Arial", 11, "bold"),
    bg="#2B00FF",
    fg="white",
    padx=30,
    pady=8
)
botao_converter.pack(pady=15)


label_resultado = tk.Label(
    janela,
    text="0.00 USD",
    font=("Arial", 16, "bold"),
    fg="#FFFFFF"
)
label_resultado.pack(pady=5)

janela.mainloop()
