import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

#puxando a imagem do batman
Batman = tk.PhotoImage(file='janela básica/img/batman.png')

# em eguida, criando um label para exibir a imagem
label = tk.LabeL(root,image=Batman)
label.pack(expand=True)

root.mainloop()