from tkinter import Tk, Canvas
from tkinter import Tk

janela = Tk()
janela.title("Senai - Sistemas")
janela.geometry("575x475")
canvas = Canvas(janela, width=500, height=400, bg="#FFFFFF")
canvas.create_rectangle(50, 50, 300, 370, fill="white")


CORES = {
    "Preto": "#000000",
    "Marrom": "#8B4513",
    "Vermelho": "#FF0000",
    "Laranja": "#FF8C00",
    "Amarelo": "#FFD700",
    "Verde": "#008000",
    "Azul": "#0000FF",
    "Violeta": "#8A2BE2",
    "Cinza": "#808080",
    "Branco": "#FFFFFF"
}


canvas.pack()
janela.mainloop()