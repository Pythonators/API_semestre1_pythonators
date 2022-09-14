from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


janela = Tk()
janela.geometry('480x800+900+20')
janela.resizable(0,0)


main_frame = Frame(janela)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame, bg='red')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

second_frame = Frame(my_canvas)


my_canvas.create_window((0,0), window=second_frame, anchor=NW)

style = Style(janela)
style.configure("TRadiobutton",font='Arial 16')
canvas = Canvas(janela)
scrolly = Scrollbar(janela, orient='vertical', command=canvas.yview)
#Variaveis---------------------------------------------------
pri = IntVar()
seg = IntVar()
tri = IntVar()
quar = IntVar()
quin = IntVar()

MODES = [('Extremamente ', 1),
        ('Muito', 2),
        ('Pouco', 3),
        ('Nada', 4),]


#Perguntas----------------------------------------------------
l_text= Label(second_frame, justify='left', font='Ivy 18', wraplength=450,
                text='1 - O avaliado fez entregas pontualmente')
l_text.pack( anchor=NW, padx=15, pady=5)

for text,mode in MODES:
    Radiobutton(second_frame, text=text, variable=pri, value=mode).pack( anchor=NW, padx=15, pady=5)

l_text1= Label(second_frame, justify='left', font='Ivy 18', wraplength=450,
                text='2 - O avaliado fez entregas de acordo com as propostas da sprint')
l_text1.pack( anchor=NW, padx=15, pady=5)

for text,mode in MODES:
    Radiobutton(second_frame, text=text, variable=seg, value=mode).pack( anchor=NW, padx=15, pady=5)

l_text2= Label(second_frame, justify='left', font='Ivy 18', wraplength=450,
                text='3 - O avaliado teve um bom desempenho no trabalho em equipe')
l_text2.pack( anchor=NW, padx=15, pady=5)

for text,mode in MODES:
    Radiobutton(second_frame, text=text, variable=tri, value=mode).pack( anchor=NW, padx=15, pady=5)

l_text3= Label(second_frame, justify='left', font='Ivy 18', wraplength=450,
                text='4 - O avaliado demonstrou habilidades e/ou desejo em se desenvolver nas tecnologias usadas no projeto')
l_text3.pack( anchor=NW, padx=15, pady=5)

for text,mode in MODES:
    Radiobutton(second_frame, text=text, variable=quar, value=mode).pack( anchor=NW, padx=15, pady=5)

l_text4= Label(second_frame, justify='left', font='Ivy 18', wraplength=450,
                text='5 - O avaliado teve uma comunicação clara com o grupo quanto às suas dificuldades e evoluções no decorrer das sprints')
l_text4.pack( anchor=NW, padx=15, pady=5)

for text,mode in MODES:
    Radiobutton(second_frame, text=text, variable=quin, value=mode).pack( anchor=NW, padx=15, pady=5)

i_peso = Image.open('imagens/botao.png')
i_peso = i_peso.resize((420,90), Image.ANTIALIAS)
i_peso = ImageTk.PhotoImage(i_peso)
but = Button(second_frame,  image=i_peso, width=100, command= janela.destroy)
but.pack(anchor=NW, padx=15, pady=15)

janela.mainloop()
