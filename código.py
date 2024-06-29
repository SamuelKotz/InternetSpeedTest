from tkinter import *


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

cor_logo = Frame(janela, width=350, height=60, bg=co5)
cor_logo.grid(column=0, row=0)



janela.mainloop()