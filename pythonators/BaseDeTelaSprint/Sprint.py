from cProfile import label
from tkinter import *
import urllib.request as url
url.urlretrieve("https://i.imgur.com/eMrv85A.png", "eMrv85A.png")
url.urlretrieve('https://i.imgur.com/1l3ru7B.png','1l3ru7B.png')
url.urlretrieve('https://i.imgur.com/mi2yAXD.png','mi2yAXD.png')
url.urlretrieve('https://i.imgur.com/yuPYZhj.png','yuPYZhj.png')
url.urlretrieve('https://i.imgur.com/GI14GMi.png','GI14GMi.png')
url.urlretrieve('https://i.imgur.com/Bl10WW5.png','Bl10WW5.png')
url.urlretrieve('https://i.imgur.com/UafmJv7.png','UafmJv7.png')
url.urlretrieve('https://i.imgur.com/UafmJv7.png','UafmJv7.png')
url.urlretrieve('https://imgur.com/a/6xOEsBt.png','6xOEsBt.png')
from tkinter import messagebox
def AbrirJanela():
     # config e design janela root
     window = Tk()
     window.title('Tela sprint')
     window.configure(bg="#F0F0F0")

    # descobrindo o tamanho da tela do usuário
     largura_screen = window.winfo_screenwidth()
     altura_screen = window.winfo_screenheight()
     largura = largura_screen+20
     altura = altura_screen+1
     posx = largura_screen/2-largura/2
     posy = altura_screen/2-altura/2

     # definindo largura e altura com base na tela do usuário
     window.geometry('%dx%d+%d+%d' % (largura_screen,altura_screen,posx,posy))

     # Texto de recepção ao usuário
     create_text = Label(text="OLÁ, SEJA BEM VINDO! \n SELECIONE SPRINT LIBERADA PARA AVALIAÇÃO.",
          justify=CENTER, font=("Inter-Regular", int(18.0)))
     create_text.place(relx=0.5, rely=0.2, anchor=CENTER)

     # Barra superior

     canvas=Canvas(window,
     height=window.winfo_screenheight(),
     width=window.winfo_screenwidth())

     canvas.place(x=0,y=0)

     canvas.create_rectangle(0.0, 0.0, 3000.0, 69.0, fill="#D9D9D9", outline="")
     
          programador = PhotoImage(file="eMrv85A.png")
     label_sprint = Label(image=sprint)
     sprint.image = sprint
     b0 = Button( image=sprint, borderwidth=0, highlightthickness=0, command = open)
     b0.place(relx=0.0, rely=0.0, width=251, height=251)
     


     # sprint 1
     create_text = Label( text="DISPONÍVEL A PARTIR DE 29/08/2022 \n ATÉ 18/09/2022",
          font=("None", int(10.0)))
     create_text.place(relx=0.04, rely=0.75)

     sprint = PhotoImage(file="eMrv85A.png")
     label_sprint = Label(image=sprint)
     sprint.image = sprint
     b0 = Button( image=sprint, borderwidth=0, highlightthickness=0, command = open)
     b0.place(relx=0.04, rely=0.4, width=251, height=251)

     # sprint 2
     create_text = Label(text="DISPONÍVEL A PARTIR DE 19/09/2022 \n ATÉ 09/10/2022",
          font=("None", int(10.0)))
     create_text.place(relx=0.29, rely=0.75)
     img2 = PhotoImage(file="GI14GMi.png")
     label_img2 = Label(window, image=img2)
     label_img2.place(relx=0.29, rely=0.4)

     # sprint 3
     create_text = Label( text="DISPONÍVEL A PARTIR DE 17/10/2022 \n ATÉ 06/11/2022",
          font=("None", int(10.0)))
     create_text.place(relx=0.53, rely=0.75)
     img3 = PhotoImage(file="mi2yAXD.png")
     label_img3 = Label(window, image=img3)
     label_img3.place(relx=0.53, rely=0.4)

     # sprint 4
     create_text = Label(text="DISPONÍVEL A PARTIR DE 07/11/2022 \n ATÉ 27/11/2022",
          font=("None", int(10.0)))
     create_text.place(relx=0.77, rely=0.75)
     img4 = PhotoImage(file="Bl10WW5.png")
     label_img4 = Label(window, image=img4)
     label_img4.place(relx=0.77, rely=0.4)

     window.resizable(False, False)
     window.mainloop()
