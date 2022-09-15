from tkinter import CENTER, Label, Tk, Canvas, Entry, Text, Button, PhotoImage
import urllib.request as url
from pythonators.PaginaVerificacao.index import AbrirJanelaAvaliacao
#from BaseDeTelaSprint.Sprint import AbrirJanelaSprint
url.urlretrieve("https://imgur.com/Mz49sv3.png", "Mz49sv3.png")
url.urlretrieve("https://imgur.com/Wc3w3RC.png", "Wc3w3RC.png")
url.urlretrieve("https://imgur.com/mZksvEC.png", "mZksvEC.png")
url.urlretrieve("https://imgur.com/TDDApv6.png", "TDDApv6.png")
url.urlretrieve("https://imgur.com/kkp1TSg.png", "kkp1TSg.png")
url.urlretrieve("https://imgur.com/qdRhJAJ.png", "qdRhJAJ.png")
url.urlretrieve("https://imgur.com/NgZ8Y0X.png", "NgZ8Y0X.png")
url.urlretrieve("https://imgur.com/qdRhJAJ.png", "qdRhJAJ.png")


def AbrirJanelaSelecionarUser():

    # ---------------------------CONFIGURAÇÃO----------------------------------

    window3 = Tk()
    window3.title("Selecionar para Avaliação")
    window3.configure(bg="#F0F0F0")

    # -----------------------TAMANHO DA TELA-----------------------------------
    largura_screen = window3.winfo_screenwidth()
    altura_screen = window3.winfo_screenheight()
    largura = largura_screen + 20
    altura = altura_screen + 1
    posx = largura_screen / 2 - largura / 2
    posy = altura_screen / 2 - altura / 2

    window3.geometry('%dx%d+%d+%d' % (largura_screen, altura_screen, posx, posy))


    canvas = Canvas(
        window3,
        bg="#F0F0F0",
        height=window3.winfo_screenheight(),
        width=window3.winfo_screenwidth(),
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0,)

    # --------------------------TEXTO DA TELA-------------------------------------------

    texto_1 = Label(window3, text="SELECIONAR QUEM VOCÊ DESEJA AVALIAR",
                    font=("Inter Regular", 48 * -1))
    texto_1.place(relx=0.5, y=160, anchor=CENTER)

    # --------------------------BARRA SUPERIOR-------------------------------------------
    canvas.create_rectangle(
        0.0,
        0.0,
        3000.0,
        69.0,
        fill="#D9D9D9",
        outline="")

    def btn_clicked_selecionarusuario():
        window3.destroy()
        AbrirJanelaAvaliacao()

    button_image_1 = PhotoImage(
        file=("Mz49sv3.png"))
    button_1 = Button(window3,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= btn_clicked_selecionarusuario,
        relief="flat"
    )
    button_1.place(
        relx=0.68,
        rely=0.65,
        width=208.0,
        height=208.0
    )


    canvas.create_text(
        1081.0,
        790.0,
        anchor="nw",
        text="LUIS INACIO",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_2 = PhotoImage(
        file=("Wc3w3RC.png"))
    button_2 = Button(window3,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        relx=0.32,
        rely=0.65,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        490.0,
        790.0,
        anchor="nw",
        text="ALINE VANNUCCI",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_3 = PhotoImage(
        file=("mZksvEC.png"))
    button_3 = Button(window3,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        relx=0.5,
        rely=0.65,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        770.0,
        790.0,
        anchor="nw",
        text="PEDRO SCOOBY",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_4 = PhotoImage(
        file=("TDDApv6.png"))
    button_4 = Button(window3,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        relx=0.14,
        rely=0.65,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        225.0,
        790.0,
        anchor="nw",
        text="RYAN COBALT",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_5 = PhotoImage(
        file=("kkp1TSg.png"))
    button_5 = Button(window3,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        relx=0.68,
        rely=0.3,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        1060.0,
        488.0,
        anchor="nw",
        text="FELIPE SANTOS",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_6 = PhotoImage(
        file=("qdRhJAJ.png"))
    button_6 = Button(window3,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        relx=0.5,
        rely=0.3,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        746.0,
        488.0,
        anchor="nw",
        text="SAMANTA ESPANHA",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_7 = PhotoImage(
        file=("NgZ8Y0X.png"))
    button_7 = Button(window3,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        relx=0.32,
        rely=0.3,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        495.0,
        488.0,
        anchor="nw",
        text="RODRIGO FARO",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_8 = PhotoImage(
        file=("qdRhJAJ.png"))
    button_8 = Button(window3,
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        relx=0.14,
        rely=0.3,
        width=208.0,
        height=208.0
    )

    canvas.create_text(
        210.0,
        488.0,
        anchor="nw",
        text="CAROLINA SASAKI",
        fill="#000000",
        font=("Inter", 24 * -1)
    )
    #def bt_voltar():
        #window3.destroy()
        #AbrirJanelaSprint()

    button_voltar = PhotoImage(file=("button_9,png"))
    button_voltar = Button(window3,
        image=button_voltar,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command= 'bt_voltar',
        relief="flat"
    )

    button_voltar.place(
        x=0.0,
        y=0.0,
        width=161.0,
        height=68.0
    )


    window3.resizable(0, 0)
    window3.mainloop()
