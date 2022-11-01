from flask import Flask, flash, render_template, request, redirect, json, session
from connect import *
from connectAluno import mostrarTodosAlunos    
from connectAvaliacao import mostrarTodos2, inserir2
from connectSala import mostrarSalas, inserirSala
from connectSprint import *
from connectTime import *
from connectAluno import *
from modelos import Alunos, Professor, Avaliacao, Salas, Times
from tinydb import TinyDB, Query
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A1B2C3'

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

#Login e autenticação

@app.route('/', methods = ['GET','POST'])
def pagina_login():
    return render_template("index.html")

@app.route('/autenticar', methods = ['GET','POST'])
def autenticar():
    Q = Query()
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    result = json.dumps(mostrarTodos())
    
    print(usuario, senha)
    if usuario == 'admin' and senha == '1234':
        session['adminlogado'] = "admin"
        return redirect("/admin")
    if bdProfessor.search(Q.usuario == usuario) and bdProfessor.search(Q.senha == senha):
        session["usuario_logado"] = request.form['nome']
        return redirect('/sprint')
    if bdAlunos.search(Q.usuario == usuario) and bdAlunos.search(Q.senha == senha):
        session["usuario_logado"] = request.form['nome']
        return redirect('/sprint')
    else:
         return redirect("/")
    
#Logout

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    session['adminlogado'] = None
    return redirect('/')

#Página de Sprint

@app.route('/sprint', methods = ['GET','POST'])
def pagina_sprint():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    sprints = mostrarSprint()
    print(sprints)
    return render_template("sprint.html",sprints=sprints)

#Página de admin (cadastro Salas)

@app.route('/admin')
def pagina_admin():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin.html",
    result=result,salas=salas)
    
#Adicionar Salas, requisição e inserção para o banco
    
@app.route('/addSalas', methods=["POST","GET"])
def addSalas():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    sala = request.form["sala"]
    TinyDB(f'Salas/{sala}.json')
    n_sala = Salas(sala)
    inserirSala(n_sala)
    return redirect("/admin")

'''@app.route('/admin/<string:sala>')
def index(sala):
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin_professores.html",
    result=result, salas=salas)'''
    
    
#Admin cadastro professores
    
@app.route('/admin/cadastro/professores')
def index():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin_professores.html",
    result=result, salas=salas)

#Inserção professor no Banco de dados

@app.route('/admin/cadastro/cadastrar', methods=["POST","GET"])
def cadastrar_professor():
    myid = uuid.uuid1()
    id = str(myid)
    cargo = request.form["cargo"]
    nome = request.form["nome"]
    usuario = request.form["usuario"]
    senha = request.form["senha"]   
    funcao = request.form["funcao"]
    professor = Professor(id,cargo,nome,usuario,senha,funcao)
    inserir(professor)
    return redirect("/admin/cadastro/professores")

#Atualizar dados professores

@app.route('/atualizar/<string:id>',methods=["POST","GET"])
def atualizar_professor(id):
    if request.method =='POST':
        id = id
        cargo = request.form["cargo"]
        nome = request.form["nome"]
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        funcao = request.form["funcao"]
        pessoa = Professor(id,cargo,nome,usuario,senha,funcao)
        try:
            atualizarProfessor(id,pessoa)
            return redirect('/admin')
        except:
            return 'algo deu errado'
    else:
        pessoa = buscarPorId(id)
        return render_template('update.html',pessoa = pessoa)

#Deletar professores do banco de dados

@app.route('/deletar/<string:id>')
def deletar(id):
    try:
        deletarProfessor(id)
        return redirect("/admin/cadastro/professores")
    except:
        return "Algo de errado aconteceu"

    #b = cargoUsuario
    #json_obj = json.loads(result)
    ob = json.dumps(result)
    json_obj = json.loads(ob)
    return render_template("avaliacao.html", result = result, perguntas = perguntas)

#Avaliação dos alunos

@app.route("/aluno/avaliacao",)
def avaliacao():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    result = mostrarTodos()
    #b = cargoUsuario
    #json_obj = json.loads(result)
    ob = json.dumps(result)
    json_obj = json.loads(ob)
    return render_template("avaliacao.html", result = result, perguntas = perguntas)

#Notas Alunos

@app.route("/aluno/notas",methods=['POST'])
def aluno_notas():
        x = 0
        y = 0
        lista = [1,2,3,4]
        option = []
        result = json.dumps(mostrarTodos())
        uniao = []
        ob = json.loads(result)
        # json_obj = json.loads(ob)
        nomesAlunos = []
        sub = []
        perguntas = []
        result2 = len(perguntas)
        for x in range(len(ob)):
            option.append([ob[x]['nome']])
            for y in range(len(lista)):
               option[x].append(request.form[ob[x]['nome']+str(lista[y])])
               y += 1
            x+=1
        for z in range(len(option)):
            avaliado = Avaliacao(option[z][0], option[z])
            inserir2(avaliado)
            z += 1
        result = mostrarTodos2()
        print(result)




            # avaliado = Avaliacao(ob[x]['nome'], option[1])
            # inserir2(avaliado)
            # result = mostrarTodos2()
            # print(result)





        #
        #         # option = request.form[str(alunos[x].nome+perguntas[y].name)]
        #         x+=1
        # print(option)


        return result
    # # sh['A' + str(2)] = option
    # print(option)

# Tela de professores

@app.route('/professor')
def professorm2():
    return render_template("tela_do_professor.html")

#Dashboard Professores

@app.route("/professor/dashboard")
def professor_dash():
    return "<h1>página dashboard</h1>"


#Admin cadastro times
    
@app.route('/admin/cadastro/times')
def cadastrotimes():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos_times()
    return render_template("admin_times.html",
    result=result)

#Inserção times no Banco de dados

@app.route('/admin/cadastro/cadastrartimes', methods=["POST","GET"])
def cadastrar_times():
    myid = uuid.uuid1()
    id = str(myid)
    turma = request.form["turma"]
    nome_time = request.form["nome_time"]
    time = Times(id,turma,nome_time)
    inserir_time(time)
    return redirect("/admin/cadastro/times")

#Atualizar dados times

@app.route('/atualizar/<string:id>',methods=["POST","GET"])
def atualizar_times(id):
    if request.method =='POST':
        id = id
        turma = request.form["turma"]
        nome_time = request.form["nome_time"]
        time = Times(id,turma,nome_time)
        try:
            atualizarTimes(id,time)
            return redirect('/admin/cadastro/times')
        except:
            return 'algo deu errado'
    else:
        time = buscarPorIdTime(id)
        return render_template('update.html',time = time)

#Deletar times do banco de dados

@app.route('/deletar/<string:id>')
def deletarTime(id):
    try:
        deletarTime(id)
        return redirect("/admin/cadastro/times")
    except:
        return "Algo de errado aconteceu"


#Admin cadastro alunos
    
@app.route('/admin/cadastro/alunos')
def cadastroalunos():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodosAlunos()
    return render_template("admin_aluno.html",
    result=result)

#Inserção alunos no Banco de dados

@app.route('/admin/cadastro/cadastraralunos', methods=["POST","GET"])
def cadastrar_alunos():
    myid = uuid.uuid1()
    id = str(myid)
    cargo_aluno = request.form["cargo_aluno"]
    nome_aluno = request.form["nome_aluno"]
    usuario_aluno = request.form["usuario_aluno"]
    senha_aluno = request.form["senha_aluno"]
    funcao_aluno = request.form["funcao_aluno"]
    aluno = Alunos(id, cargo_aluno, nome_aluno, usuario_aluno, senha_aluno, funcao_aluno)
    inserirAlunos(aluno)
    return redirect("/admin/cadastro/alunos")

#Atualizar dados alunos

@app.route('/atualizar/<string:id>',methods=["POST","GET"])
def atualizar_alunos(id):
    if request.method =='POST':
        cargo_aluno = request.form["cargo_aluno"]
        nome_aluno = request.form["nome_aluno"]
        usuario_aluno = request.form["usuario_aluno"]
        senha_aluno = request.form["senha_aluno"]
        funcao_aluno = request.form["funcao_aluno"]
        aluno = Alunos(id, cargo_aluno, nome_aluno, usuario_aluno, senha_aluno, funcao_aluno)
        try:
            atualizarAlunos(id,aluno)
            return redirect('/admin/cadastro/alunos')
        except:
            return 'algo deu errado'
    else:
        aluno = buscarPorIdAluno(id)
        return render_template('update.html',aluno = aluno)

#Deletar alunos do banco de dados

@app.route('/deletar/<string:id>')
def deletarAlunos(id):
    try:
        deletarAlunos(id)
        return redirect("/admin/cadastro/alunos")
    except:
        return "Algo de errado aconteceu"
