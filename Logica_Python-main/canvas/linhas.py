from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")
canvas = Canvas(janela, width=400, height=300, bg="yellow")
canvas.create_line(
    10, 10, 200, 185,
    fill="black",
    width=2
)
canvas.create_line(
    10, 200, 10, 10,
    fill="black",
    width=2
)

canvas.create_line(
    200, 10, 10, 10,
    fill="black",
    width=2
)

canvas.pack()
janela.mainloop()