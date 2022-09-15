from tkinter import *
import pandas as pd
from tkinter import messagebox
from pythonators.BaseDeTelaSprint.Sprint import AbrirJanelaSprint


#consulta de login na xlsx
data = pd.read_excel('login.xlsx',engine='openpyxl')
senha1 = str(data.iloc[0,1])
email1 = str(data.iloc[0,0])


#Função verificação de login inserido e abrir página de avaliação
def btn_clickedlogin():
    emailcred = str(email.get())
    senhacred = str(senha.get())
    if (emailcred == email1) and (senhacred == senha1):
        print('Login ok')
        window.destroy()
        AbrirJanelaSprint()

    elif (emailcred != email1 or senhacred != senha1):
        messagebox.showerror(title=None, message='                         Erro!\n Seu usuário ou senha estão incorretos')

#config e design janela root
window = Tk()
window.title('Login testes')
window.configure(bg="#FFFFFF")
window.iconphoto(False, PhotoImage(file='image 1.png'))

#definindo largura e altura com base na tela do usuário

largura_screen = window.winfo_screenwidth()
altura_screen = window.winfo_screenheight()
largura = largura_screen+20
altura = altura_screen+1
posx = largura_screen/2-largura/2
posy = altura_screen/2-altura/2
window.geometry('%dx%d+%d+%d' % (largura_screen,altura_screen,posx,posy))


#Window design
create_text = Label(text="Ao clicar em entrar, ou ao continuar com as outras opções \n "
                         "abaixo, você concorda com os Termos de serviço e confirma \n "
                         "que leu a Política de privacidade do Pythonators Database.",
                    justify=CENTER,bg='#FFFFFF', font=("inter", int(13.0)))

create_text.place(relx = 0.5, rely = 0.65, anchor = CENTER)

img0 = PhotoImage(file = f"img0.png")
img1 = PhotoImage(file="image 1.png")
label_img1 = Label(window, bg='#FFFFFF', image=img1)
label_img1.place(relx = 0.5, rely = 0.17, anchor = CENTER)

#Config botão login
b0 = Button(image=img0, bg="#FFFFFF", command=btn_clickedlogin, relief="flat")
b0.place(relx = 0.5, rely = 0.75, anchor = CENTER, width=512, height=64)

#Config entrada de email e senha com placeholder

def on_click1(event):
    email.configure(state=NORMAL)
    email.delete(0, END)

def on_click2(event):
    senha.configure(state=NORMAL)
    senha.delete(0,END)

email = Entry(window, font="inter 18", bg='#D9D9D9')
email.insert(0,'USUÁRIO')
email.configure(state=DISABLED)
email.bind("<Button-1>",on_click1)
email.place(relx = 0.5, rely = 0.45, anchor = CENTER, width=518, height=50)

senha = Entry(window, font="inter 18", bg='#D9D9D9',)
senha.insert(0,'SENHA')
senha.configure(state=DISABLED)
senha.bind("<Button-1>",on_click2)
senha.place(relx=0.5, rely=0.55, anchor=CENTER, width=518, height=50)

window.resizable(False, False)
window.mainloop()
