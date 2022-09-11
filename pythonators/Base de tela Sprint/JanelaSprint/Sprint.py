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
create_text.place(relx=0.5, rely=0.2, anchor=CENTER)


img0 = PhotoImage(file=f"group_10.png")
label_img0 = Label(window, image=img0)
label_img0.place(relx=0.5, rely=0.5, width=1366, height=21, anchor=tkinter.CENTER)

img1 = PhotoImage(file=f"barra.png")
label_img1 = Label(window, image=img1)
label_img1.place(relx=0, rely=0, width=1366, height=50)


# sprint 1
create_text = Label( text="DISPONÍVEL A PARTIR DE 29/08/2022 \n ATÉ 18/09/2022",
     font=("None", int(10.0)))
create_text.place(relx=0.04, rely=0.75)

sprint = PhotoImage(file=f"button sprint 1.png")
label_sprint = Label(image=sprint)
sprint.image = sprint
b0 = Button( image=sprint, borderwidth=0, highlightthickness=0, command = open)
b0.place(relx=0.04, rely=0.4, width=251, height=251)
   
# sprint 2
create_text = Label(text="DISPONÍVEL A PARTIR DE 19/09/2022 \n ATÉ 09/10/2022",
     font=("None", int(10.0)))
create_text.place(relx=0.29, rely=0.75)
img2 = PhotoImage(file=f"button sprint 2.png")
label_img2 = Label(window, image=img2)
label_img2.place(relx=0.29, rely=0.4)

# sprint 3
create_text = Label( text="DISPONÍVEL A PARTIR DE 17/10/2022 \n ATÉ 06/11/2022",
     font=("None", int(10.0)))
create_text.place(relx=0.53, rely=0.75)
img3 = PhotoImage(file=f"button sprint 3.png")
label_img3 = Label(window, image=img3)
label_img3.place(relx=0.53, rely=0.4)

# sprint 4
create_text = Label(text="DISPONÍVEL A PARTIR DE 07/11/2022 \n ATÉ 27/11/2022",
     font=("None", int(10.0)))
create_text.place(relx=0.77, rely=0.75)
img4 = PhotoImage(file=f"button sprint 4.png")
label_img4 = Label(window, image=img4)
label_img4.place(relx=0.77, rely=0.4)

window.resizable(False, False)
window.mainloop()
