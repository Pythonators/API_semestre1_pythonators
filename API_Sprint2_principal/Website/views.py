#routes, caminhos das páginas para navegação (todas URLS)
from flask import Blueprint, render_template

views = Blueprint('views', __name__)




@views.route('/')
def pagina_login():
    return render_template("login.html")

@views.route('/sprint')
def pagina_sprint():
    return render_template("sprint.html")

@views.route('/admin')
def pagina_admin():
    return "<h1>página cadastro de alunos e grupos</h1>"

@views.route('/admin/cadastro')
def pagina_cadastro_admin():
    return render_template("admin_cadastro.html",textadmin = 'Hello, Admin')


class Aluno:
    def __init__(self, nome):
        self.nome = nome


a1 = Aluno('Caio')
a2 = Aluno('Marcelo')
a4 = Aluno('Gabriel')
a5 = Aluno('Mikaéla')
a6 = Aluno('Isadora')
a7 = Aluno('Cauana')
a8 = Aluno('Ana')
a9 = Aluno('Felipe')
a10 = Aluno('Murilo')
a11 = Aluno('Ryan')

alunos = []
alunos.append(a1), alunos.append(a2), alunos.append(a4), alunos.append(a5), alunos.append(a6), alunos.append(a7),
alunos.append(a8), alunos.append(a9), alunos.append(a10), alunos.append(a11)

class Pergunta:
    def __init__(self, pergunta_, name):
        self.pergunta_ = pergunta_
        self.name = name

p1 = Pergunta('1 - O avaliado fez entregas pontualmente', '1')
p2 = Pergunta('2 - O avaliado fez entregas de acordo com as propostas da sprint', '2')
p3 = Pergunta('3 - O avaliado teve um bom desempenho no trabalho em equipe', '3')
p4 = Pergunta('4 - O avaliado demonstrou habilidades e/ou desejo em se desenvolver nas tecnologias usadas no projeto',
              '4')
perguntas = []
perguntas.append(p1)
perguntas.append(p2)
perguntas.append(p3)
perguntas.append(p4)

@views.route("/aluno/avaliacao")
def avaliacao():
    return render_template("avaliacao.html", alunos = alunos, perguntas = perguntas)

@views.route("/aluno/notas")
def aluno_notas():
    return "<h1>Página de notas do aluno logado</h1>"

@views.route('/professor-m2')
def professorm2():
    return "<h1>página professor M2</h1>"

@views.route('/professor-p2')
def professorp2():
    return "<h1>página professor P2</h1>"

@views.route("/professor/dashboard")
def professor_dash():
    return "<h1>página dashboard</h1>"