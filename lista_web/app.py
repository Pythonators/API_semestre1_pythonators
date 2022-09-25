from flask import Flask, render_template

app = Flask(__name__)

class Aluno:
    def __init__(self, nome):
        self.nome = nome
     
a1 = Aluno('Caio')
a2 = Aluno('Marcelo' )
a3 = Aluno('Murilo')
a4 = Aluno('Gabriel')
a5 = Aluno('Micaela')
a6 = Aluno('Isadora')
a7 = Aluno('Cauana')
a8 = Aluno('Ana')
a9 = Aluno('Felipe')
a10 = Aluno('Ryan')

alunos = []
alunos.append(a1)
alunos.append(a2)
alunos.append(a3)
alunos.append(a4)
alunos.append(a5)
alunos.append(a6)
alunos.append(a7)
alunos.append(a8)
alunos.append(a9)
alunos.append(a10)

class Pergunta:
    def __init__(self, pergunta_, name):
        self.pergunta_ = pergunta_
        self.name = name
p1 = Pergunta('1 - O avaliado fez entregas pontualmente', '1')
p2 = Pergunta('2 - O avaliado fez entregas de acordo com as propostas da sprint', '2')
p3 = Pergunta('3 - O avaliado teve um bom desempenho no trabalho em equipe', '3')
p4 = Pergunta('4 - O avaliado demonstrou habilidades e/ou desejo em se desenvolver nas tecnologias usadas no projeto', '4')

perguntas = []
perguntas.append(p1)
perguntas.append(p2)
perguntas.append(p3)
perguntas.append(p4)

@app.route("/")
def index():
    return render_template("index.html", alunos = alunos, perguntas = perguntas)


if __name__ == "__main__":
    app.run(debug=True)
