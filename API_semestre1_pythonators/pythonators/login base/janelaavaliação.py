from tkinter import *


def btn_clicked():
    print("Button Clicked")


window2 = Tk()

window2.geometry("1440x3057")
window2.configure(bg = "#F0F0F0")
canvas = Canvas(
    window2,
    bg = "#F0F0F0",
    height = 3057,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    8444.5, -2.5,
    text = "1 - Quão comprometido(a) é CAROLINA SASAKI?",
    fill = "#000000",
    font = ("None", int(24.0)))

img4 = PhotoImage(file = f"img4.png")
b0 = Button(window2,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 500, y = 500,
    width = 375,
    height = 80)

canvas.create_text(
    600.5, 600.0,
    text = "VOCÊ ESTÁ AVALIANDO:",
    fill = "#000000",
    font = ("Inter-Regular", int(38.0)))

canvas.create_text(
    8570.0, -111.0,
    text = "CAROLINA SASAKI",
    fill = "#000000",
    font = ("None", int(36.0)))

img3 = PhotoImage(file = f"img3.png")
b1 = Button(window2,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 700, y = 700,
    width = 300,
    height = 90)

canvas.create_text(
    9136.5, -479.5,
    text = "PROGRAMADOR",
    fill = "#000000",
    font = ("None", int(24.0)))

canvas.create_text(
    8799.5, -479.5,
    text = "RYAN AFONSO",
    fill = "#000000",
    font = ("None", int(24.0)))

window2.resizable(False, False)
window2.mainloop()
