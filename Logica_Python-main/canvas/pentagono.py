from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")
canvas = Canvas(janela, width=400, height=300, bg="gray")
canvas.create_polygon(

    60, 50,
    10, 100,
    40, 150,
    80, 150,
    110, 100,

    fill="black",
    outline="white",
    width=2

)

canvas.pack()
janela.mainloop()