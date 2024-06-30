from tkinter import *
from PIL import Image, ImageTk
import speedtest


#cores:
co0 = "#f0f3f5"  # preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha 
co4 = "#403d3d"   # preta 
co5 = "#4a88e8"  # azul


janela = Tk()
janela.title("Internet Speed Test - By SamuelKotz")
janela.geometry('350x200')
janela.configure(background=co1)

#separação da janela em cores para icons da parte superior

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

#teste de velocidade de internet
def test():
    speed = speedtest.Speedtest()
    download = '{:.2f}'.format(speed.download() / 1024 / 1024)
    upload = '{:.2f}'.format(speed.upload() / 1024 / 1024)

    download_t["text"] = download
    upload_t["text"] = upload
    botao["text"] = "Testar novamente"


#parte inferior do programa

download_t = Label(cor_corpo, text="", anchor=NW, font=("Arial 28"), bg= co1, fg = co4)
download_t.place(x=30, y=20)
download_t2 = Label(cor_corpo, text="Mbps Download", anchor=NW, font=("Ivy 10"), bg= co1, fg = co4)
download_t2.place(x=30, y=70)

imagem_down = Image.open("seta baixo.png")
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)

down = Label(cor_corpo, image=imagem_down, height=50, compound=LEFT, bg= co1, fg = co3)
down.place(x=130, y=30)


upload_t = Label(cor_corpo, text="", anchor=NW, font=("Arial 28"), bg= co1, fg = co4)
upload_t.place(x=235, y=20)
upload_t2 = Label(cor_corpo, text="Mbps Upload", anchor=NW, font=("Ivy 10"), bg= co1, fg = co4)
upload_t2.place(x=230, y=70)

imagem_up = Image.open("seta cima.png")
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)

up = Label(cor_corpo, image=imagem_up, height=50, compound=LEFT, bg= co1, fg = co3)
up.place(x=170, y=30)

botao = Button(cor_corpo, text="Iniciar Teste", font=("Arial 10"), bg= co2, fg = co4, command=test)
botao.place(x=130, y=100)



janela.mainloop()