import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Cores
cor0 = '#FFFFFF'  # white / branca
cor1 = '#333333'  # black / preta
cor2 = '#fcc058'  # orange / laranja
cor3 = '#fff873'  # yellow / amarela
cor4 = '#34eb3d'  # green / verde
cor5 = '#e85151'  # red / vermelha
fundo = '#3b3b3b'

janela = Tk()
janela.title('pedra, papel e tesoura')
janela.geometry('270x280')  # Ajustado para 270 de largura para acomodar melhor os 3 botões
janela.configure(bg=fundo)

# Frames
frame_cima = Frame(janela, width=270, height=100, bg=cor1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=270, height=180, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando os jogadores
# Jogador pessoa
app_pessoa = Label(frame_cima, text='jogador', height=1, anchor='center', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_pessoa.place(x=10, y=70)

# Barra marcou pontos
app_pessoa_linha = Label(frame_cima, text="", height=10, anchor='center', bg=cor4, fg=cor0, font=('Ivy 10 bold'))
app_pessoa_linha.place(x=0, y=0)

# Pontuação
app_pessoa_pontos = Label(frame_cima, text='0', height=1, anchor='center', bg=cor1, fg=cor0, font=('Ivy 30 bold'))
app_pessoa_pontos.place(x=50, y=20)

# Separação da pontuação
app_vs = Label(frame_cima, text=':', height=1, anchor='center', bg=cor1, fg=cor0, font=('Ivy 30 bold'))
app_vs.place(x=130, y=20)

# Jogador PC
app_pc = Label(frame_cima, text='PC', height=1, anchor='center', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_pc.place(x=225, y=70)

# Barra marcou pontos PC
app_pc_linha = Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=265, y=0)

# Pontuação PC
app_pc_pontos = Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=180, y=20)

# Barra de empate
app_empate = Label(frame_cima, text="", width=270, anchor="center", bg=cor3, fg=cor0, font=("Ivy 1 bold"))
app_empate.place(x=0, y=95)

# Mostra a jogada do pc
app_jogada_pc = Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pc.place(x=190, y=10)

app_jogada_pessoa = Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pessoa.place(x=10, y=10)

app_vencedor = Label(frame_baixo, text="", height=1, anchor="center", bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_vencedor.place(x=40, y=-5)

pontos_pessoa = 0
pontos_pc = 0
rodadas = 5
numero_rodada = 0 

rodadas = 5

def reiniciar_jogo():

    global pontos_pessoa
    global pontos_pc
    global rodadas
    global numero_rodada

    # Zera as variáveis do jogo
    pontos_pessoa = 0
    pontos_pc = 0
    rodadas = 5
    numero_rodada = 0

    # Atualiza a pontuação na tela
    app_pessoa_pontos["text"] = "0"
    app_pc_pontos["text"] = "0"

    # Limpa as jogadas e o vencedor
    app_jogada_pessoa["text"] = ""
    app_jogada_pc["text"] = ""
    app_vencedor["text"] = ""

    # Volta as barras para a cor inicial
    app_pessoa_linha["bg"] = cor1
    app_pc_linha["bg"] = cor1
    app_empate["bg"] = cor0



def jogar(jogada):
    global escolha_pessoa
    global pontos_pessoa
    global pontos_pc
    global rodadas
    global numero_rodada

    opcoes = ["pedra", "papel", "tesoura"]

    app_pessoa_linha["bg"] = cor1
    app_pc_linha["bg"] = cor1
    app_empate["bg"] = cor0


    if rodadas > 0:

        numero_rodada += 1

        escolha_pessoa = jogada
        escolha_pc = random.choice(opcoes)

        # Mostra as jogadas
        app_jogada_pessoa["text"] = escolha_pessoa
        app_jogada_pc["text"] = escolha_pc

        rodadas -= 1

        # EMPATE
        if testa_empate(escolha_pessoa, escolha_pc):

            app_empate["bg"] = cor3

            app_vencedor["text"] = f"Rodada {numero_rodada}: EMPATE"
            app_vencedor["fg"] = cor2

        # JOGADOR GANHOU
        elif testa_vitoria_pessoa(escolha_pessoa, escolha_pc):

            pontos_pessoa += 10

            app_pessoa_linha["bg"] = cor4
            app_pessoa_pontos["text"] = str(pontos_pessoa)

            app_vencedor["text"] = f"Rodada {numero_rodada}: JOGADOR GANHOU"
            app_vencedor["fg"] = cor4

        # PC GANHOU
        else:

            pontos_pc += 10

            app_pc_linha["bg"] = cor4
            app_pc_pontos["text"] = str(pontos_pc)

            app_vencedor["text"] = f"Rodada {numero_rodada}: PC GANHOU"
            app_vencedor["fg"] = cor5

    if rodadas == 0:
        btn_reiniciar.place(x=25, y=120)
        btn_jogar.place_forget()

def iniciar_jogo():
    global icone_papel
    global icone_pedra
    global icone_tesoura
    global btn_papel
    global btn_pedra
    global btn_tesoura
    

    icone_pedra = Image.open("pedra.png")
    icone_pedra = icone_pedra.resize((50, 50), Image.Resampling.LANCZOS)
    icone_pedra = ImageTk.PhotoImage(icone_pedra)
    btn_pedra = Button(frame_baixo, command=lambda: jogar("pedra"), width=50, height=50, image=icone_pedra, bg=cor0, relief="flat")
    btn_pedra.place(x=25, y=50)

    icone_papel = Image.open("papel.png")
    icone_papel = icone_papel.resize((50, 50), Image.Resampling.LANCZOS)
    icone_papel = ImageTk.PhotoImage(icone_papel)
    btn_papel = Button(frame_baixo, command=lambda: jogar("papel"), width=50, height=50, image=icone_papel, bg=cor0, relief="flat")
    btn_papel.place(x=105, y=50)

    icone_tesoura = Image.open("tesoura.png")
    icone_tesoura = icone_tesoura.resize((50, 50), Image.Resampling.LANCZOS)
    icone_tesoura = ImageTk.PhotoImage(icone_tesoura)
    btn_tesoura = Button(frame_baixo, command=lambda: jogar("tesoura"), width=50, height=50, image=icone_tesoura, bg=cor0, relief="flat")
    btn_tesoura.place(x=185, y=50)





btn_jogar = Button(frame_baixo, text="Jogar", width=24, height=1, bg=cor1, fg=cor0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge", command=iniciar_jogo)
btn_jogar.place(x=25, y=120)

btn_reiniciar = Button(frame_baixo, text="Reiniciar", width=24, height=-1, bg=cor1, fg=cor0, font=("Ivy 10 bold"), relief="raised", overrelief="ridge", command=reiniciar_jogo)


def testa_empate(escolha_pessoa, escolha_pc):
    if escolha_pc == escolha_pessoa:
        return True
    return False

def testa_vitoria_pessoa(escolha_pessoa, escolha_pc):
    if (
        (escolha_pessoa == "pedra" and escolha_pc == "tesoura")
        or (escolha_pessoa == "papel" and escolha_pc == "pedra")
        or (escolha_pessoa == "tesoura" and escolha_pc == "papel")
    ):
        return True
    return False

   

janela.mainloop()