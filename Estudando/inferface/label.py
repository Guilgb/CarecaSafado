from tkinter import *


def funcao_botao(self):
    label_1["text"] = "Botão foi pressionado"


janela = Tk()

label_1 = Label(janela, text="Estudando Label", font="Arial 20")

janela.geometry("1920x1080+0+0")
label_1.place(x=50, y=200)

botao_1 = Button(janela, width=230, text="Botão",
                 command=funcao_botao, background="blue")
botao_1.place(x=50, y=250)
janela.mainloop()
