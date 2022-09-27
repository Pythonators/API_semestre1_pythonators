from flask import Blueprint

#Rotas

auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    return

@auth.route("/sprint")
def pagina_sprint():
    mensagem = "o botão foi acionado"
    return ("<p>página sprint<\p>",mensagem)

@auth.route('/admin')
def pagina_admin():
    return "<p>página admin<\p>"

@auth.route('/admin/cadastro')
def pagina_cadastro_admin():
    return "<p>página cadastro de alunos e grupos<\p>"

@auth.route("/aluno/avaliacao")
def avaliacao():
    return "<p>página de avaliação aluno<\p>"

@auth.route("/aluno/notas")
def aluno_notas():
    return "<p>página de notas aluno<\p>"

@auth.route('/professor-m2')
def professorm2():
    return "<p>página professor M2<\p>"

@auth.route('/professor-p2')
def professorp2():
    return "<p>página professor P2<\p>"

@auth.route("/professor/dashboard")
def professor_dash():
    return "<p>página dashboard<\p>"