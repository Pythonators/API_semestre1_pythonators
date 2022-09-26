from flask import Blueprint

#Rotas

auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    return

@auth.route("/sprint")
def pagina_sprint():
    return "<p>página sprint<\p>"
    #mensagem="o botão foi acionado"
    #linkar botão aqui

@auth.route('/admin')
def pagina_admin():
    return "<p>página admin<\p>"

@auth.route('/admin/cadastro')
def pagina_cadastro_admin():
    return "<p>página cadastro de alunos e grupos<\p>"

@auth.route("/aluno")
def telaavaliacao():
    return "<p>página aluno<\p>"

@auth.route('/professor-m2')
def pagina_professorm2():
    return "<p>página professor M2<\p>"

@auth.route('/professor-p2')
def pagina_professorp2():
    return "<p>página professor P2<\p>"

@auth.route("/professor/dashboard")
def pagina_professor_dash():
    return "<p>página dashboard<\p>"




