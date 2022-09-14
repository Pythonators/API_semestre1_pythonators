from cgitb import text
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import CENTER, Label, Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# ---------------------------CONFIGURAÇÃO----------------------------------

window = Tk()
window.title("Selecionar para Avaliação")
window.configure(bg="#F0F0F0")

# -----------------------TAMANHO DA TELA-----------------------------------
width_value = window.winfo_screenwidth()
height_value = window.winfo_screenheight()
window.geometry("%dx%d" % (width_value, height_value))


canvas = Canvas(
    window,
    bg="#F0F0F0",
    height=window.winfo_screenheight(),
    width=window.winfo_screenwidth(),
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0,)

# --------------------------TEXTO DA TELA-------------------------------------------

texto_1 = Label(window, text="SELECIONAR QUEM VOCÊ DESEJA AVALIAR",
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


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    file=relative_to_assets("button_2.png"))
button_2 = Button(
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
    file=relative_to_assets("button_3.png"))
button_3 = Button(
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
    file=relative_to_assets("button_4.png"))
button_4 = Button(
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
    file=relative_to_assets("button_5.png"))
button_5 = Button(
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
    file=relative_to_assets("button_6.png"))
button_6 = Button(
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
    file=relative_to_assets("button_7.png"))
button_7 = Button(
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
    file=relative_to_assets("button_8.png"))
button_8 = Button(
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

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    bg="#D9D9D9",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)

button_9.place(
    x=0.0,
    y=0.0,
    width=161.0,
    height=68.0
)

window.resizable(0, 0)
window.mainloop()
