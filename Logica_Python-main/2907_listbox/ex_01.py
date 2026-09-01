# Exercício - Calculadora de IMC
# Requisitos: Widgets Básicos, Use Label, entry e button
# Campos de entrada: Dois entry: peso(kg) e altura(m)
# Botão celular: botão que calcula o IMC e exibe o resultado e mum label
# Faixa do IMC: exibir mensagem. Abaixo do peso, Saudavel. sobrepeso ou obesidade

import tkinter as tk

def calcular_imc():
    try:

        peso = float(entry_peso.get().replace(',', '.'))
        altura = float(entry_altura.get().replace(',', '.'))
        

        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            faixa = "Abaixo do peso"
        elif imc < 25.0:
            faixa = "Saudável"
        elif imc < 30.0:
            faixa = "Sobrepeso"
        else:
            faixa = "Obesidade"
            

        label_resultado.config(text=f"IMC: {imc:.2f}\nClassificação: {faixa}")
    except ValueError:

        label_resultado.config(text="Por favor, insira valores válidos.")


janela = tk.Tk()
janela.title("Senai - Sistemas")
janela.geometry("800x600")


label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack(pady=5)
entry_peso = tk.Entry(janela)
entry_peso.pack()


label_altura = tk.Label(janela, text="Altura (m):")
label_altura.pack(pady=5)
entry_altura = tk.Entry(janela)
entry_altura.pack()


botao_calcular = tk.Button(janela, text="Calcular", command=calcular_imc)
botao_calcular.pack(pady=15)

aviso = tk.Label(janela, text = "Preencha o campo e clique em calcular. ", font=("Arial", 14))
aviso.pack(pady=20)


label_resultado = tk.Label(janela, text="", font=("Arial", 11, "bold"))
label_resultado.pack(pady=10)

janela.mainloop()
