from cProfile import label
from tkinter import *
from tkinter import messagebox

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
create_text.place(x=700, y=100, anchor=CENTER)


img0 = PhotoImage(file=f"group_10.png")
label_img0 = Label(window, image=img0)
label_img0.place(x=320, y=400)

img1 = PhotoImage(file=f"barra.png")
label_img1 = Label(window, image=img1)
label_img1.place(x=0, y=0)


# sprint 1
create_text = Label( text="DISPONÍVEL A PARTIR DE 29/08/2022 \n ATÉ 18/09/2022",
     font=("None", int(10.0)))
create_text.place(x=40, y=584)

sprint = PhotoImage(file=f"button sprint 1.png")
label_sprint = Label(image=sprint)
sprint.image = sprint
b0 = Button( image=sprint, borderwidth=0, highlightthickness=0, command = open)
b0.place(x=40, y=300, width=251, height=251)
   
# sprint 2
create_text = Label(text="DISPONÍVEL A PARTIR DE 19/09/2022 \n ATÉ 09/10/2022",
     font=("None", int(10.0)))
create_text.place(x=370, y=584)
img2 = PhotoImage(file=f"button sprint 2.png")
label_img2 = Label(window, image=img2)
label_img2.place(x=370, y=300)

# sprint 3
create_text = Label( text="DISPONÍVEL A PARTIR DE 17/10/2022 \n ATÉ 06/11/2022",
     font=("None", int(10.0)))
create_text.place(x=700, y=584)
img3 = PhotoImage(file=f"button sprint 3.png")
label_img3 = Label(window, image=img3)
label_img3.place(x=700, y=300)

# sprint 4
create_text = Label(text="DISPONÍVEL A PARTIR DE 07/11/2022 \n ATÉ 27/11/2022",
     font=("None", int(10.0)))
create_text.place(x=1038, y=584)
img4 = PhotoImage(file=f"button sprint 4.png")
label_img4 = Label(window, image=img4)
label_img4.place(x=1038, y=300)

window.resizable(False, False)
window.mainloop()
