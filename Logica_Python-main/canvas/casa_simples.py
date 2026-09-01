from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("400x300")
canvas = Canvas(janela, width=400, height=300, bg="blue")

# Texto
canvas.create_text(195,20, text='Casa simples', font=('arial', 16, "bold"), fill='white')


# Grama
canvas.create_rectangle(
   0, 300, 800, 250,
    fill="green",
    outline="green"
)

# Quadrado da casa
canvas.create_rectangle(
    140, 140, 250, 250,
    fill="yellow",
    outline="Black"
)

# Telhado da casa
canvas.create_polygon(
    195, 40, 250, 140, 140, 140,
    fill="red",
    outline="black"
)

# Porta da casa
canvas.create_rectangle(
    180, 197, 210, 250,
    fill="brown",
    outline="Black",
    width=2
)

# Janela da casa - lado esquerdo
canvas.create_rectangle(
    150, 160, 175, 185,
    fill="white",
    outline="Black"
)

# Linha Vertical da Janela esquerda
canvas.create_line(
    161, 160, 161, 185,
    fill="black",
    width=1
)

# Linha Horizontal da Janela esquerda 
canvas.create_line(
    150, 172, 175, 172,
    fill="black",
    width=1
)

# Janela da casa - lado direito
canvas.create_rectangle(
    215, 160, 240, 185,
    fill="white",
    outline="Black"
)

# Linha Vertical da Janela direita
canvas.create_line( 
    227, 160, 227, 185, 
    fill="black",
    width=1 
)

# Linha Horizontal da Janela direita
canvas.create_line( 
    215, 172, 240, 172, 
    fill="black", 
    width=1 
)

# Maçaneta da porta
canvas.create_oval(
    182, 220, 187, 222,
    fill="black"
)

canvas.pack()
janela.mainloop()