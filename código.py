from tkinter import *
from PIL import Image, ImageTk


#cores:
co0 = "#f0f3f5"  # preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha 
co4 = "#403d3d"   # preta 
co5 = "#4a88e8"  # azul


janela = Tk()
janela.title = "Internet Speed Test - By SamuelKotz"
janela.geometry('350x200')
janela.configure(background=co1)

#separação da janela em cores para icons

cor_logo = Frame(janela, width=350, height=60, bg=co1)
cor_logo.grid(column=0, row=0)

cor_corpo = Frame(janela, width=350, height=140, bg=co1)
cor_corpo.grid(column=0, row=1)

imagem = Image.open("internet.png")
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

logo = Label(cor_logo, image=imagem, height=50, compound=LEFT, bg= co1, fg = co3)
logo.place(x=20, y=0)

nome = Label(cor_logo, text="Teste de Velocidade de Internet", height=60, compound=LEFT, padx=10, anchor=NE, font=("Arial"), bg= co1, fg = co4)
nome.place(x=75, y=10)

linha_divisoria = Label(cor_logo, width=350, height=60, compound=LEFT, anchor=NW, font=("Arial 1"), bg= co2)
linha_divisoria.place(x=0, y=57)


janela.mainloop()