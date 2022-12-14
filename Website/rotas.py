from flask import Flask, flash, render_template, request, redirect, json, session
from connect import mostrarTodos, inserir, atualizarProfessor, buscarPorId, deletarProfessor, bdProfessor
from connectAluno import mostrarTodosAlunos, bdAlunos
from connectAvaliacao import mostrarTodos2, inserir2
from connectSala import mostrarSalas, inserirSala, deletarSala, atualizarSala, buscarPorNomeSala
from connectSprint import *
from connectTime import *
from connectAluno import *
from modelos import Alunos, Professor, Avaliacao, Salas, Times
from tinydb import TinyDB, Query
import uuid
import json
import numpy as np


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
p5 = Pergunta('5 - O avaliado teve uma comunicação clara com o grupo quanto às suas dificuldades e evoluções no decorrer das sprints',
              '5')
perguntas = []
perguntas.append(p1)
perguntas.append(p2)
perguntas.append(p3)
perguntas.append(p4)
perguntas.append(p5)


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
    ob = json.loads(result)
    if usuario == 'admin' and senha == '1234':
        session['adminlogado'] = "admin"
        return redirect("/admin")
    if bdProfessor.search(Q.usuario == usuario) and bdProfessor.search(Q.senha == senha):
        session["usuario_logado"] = request.form['nome']
        session['tipo'] = "PROFESSOR"

        return redirect('/sprint')
    if bdAlunos.search(Q.usuario == usuario) and bdAlunos.search(Q.senha == senha):
        session["usuario_logado"] = request.form['nome']
        session['tipo'] = "ALUNO"
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
    
    selecionado = sprints[2]['sprint']#controle intracódigo para qual sprint está aberta, ela vai direto para o banco de avaliações.
    session['sprint_atual'] = selecionado#session pra usar no banco de avaliações

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
    mostrar_salas = mostrarSalas()
    return render_template("admin_turmas.html",
    result=result,sala=mostrar_salas)


@app.route('/deletar/sala/<string:sala>', methods = ['GET','POST'])
def deletarSalas(sala):
    try:
        deletarSala(sala)
        return redirect("/admin")
    except:
        return "Algo de errado aconteceu"
    
@app.route('/admin/<string:sala>', methods = ['GET','POST'])
def attSala(sala):
    if request.method =='POST':
        sala = request.form["sala"]
        p2 = request.form["p2"]
        m2 = request.form["m2"]
        turma = Salas(sala,p2,m2)
        try:
            atualizarSala(sala,turma)
            return redirect('/admin')
        except:
            return 'algo deu errado'
    else:
        result = mostrarTodos()
        turma = buscarPorNomeSala(sala)
        return render_template('update_sala.html',turma = turma, result = result)

    
#Adicionar Salas, requisição e inserção para o banco
    
@app.route('/addSalas', methods=["POST","GET"])
def addSalas():
    # Q = Query()
    # if 'usuario_logado' in session:
    #     redirect("/")
    # if 'adminlogado' not in session or session['adminlogado'] == None:
    #     return redirect('/')

    sala = request.form["sala"]
    prof = request.form['p2']
    prof2 = request.form['m2']
    sala = Salas(sala,prof,prof2)
    inserirSala(sala)
    return redirect ("/admin")
    #teste com o flashcard caso a sala já exista
    '''if bd.search(Q.sala != sala):
        n_sala = Salas(sala, prof, prof2)
        inserirSala(n_sala)
        TinyDB(f'Salas/{sala}.json')
    else:
        flash('Essa sala já existe!')'''



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
    nome = request.form["nome"]
    usuario = request.form["usuario"]
    senha = request.form["senha"]   
    #funcao = request.form["funcao"]
    professor = Professor(id,nome,usuario,senha)
    inserir(professor)
    return redirect("/admin/cadastro/professores")

#Atualizar dados professores

@app.route('/atualizar/<string:id>',methods=["POST","GET"])
def atualizar_professor(id):
    if request.method =='POST':
        id = id
        nome = request.form["nome"]
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        pessoa = Professor(id,nome,usuario,senha)
        try:
            atualizarProfessor(id,pessoa)
            return redirect('/admin/cadastro/professores')
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
    
    bd_avaliacao = TinyDB("Avaliacao.json")
    Q = Query()

    todos_avaliacao = bd_avaliacao.all()
    ob_avaliacao = json.dumps(todos_avaliacao)
    json_avaliacao = json.loads(ob_avaliacao)
    x = json_avaliacao

    nomes_avaliacao = []

    for i in range(len(x)):
        nomes_avaliacao.append(x[i]["avaliador"])
    print(nomes_avaliacao)
    
    for n in range(len(nomes_avaliacao)):
        if nomes_avaliacao[n] == session['usuario_logado']:
            return render_template('finalizaçao.html')

    result = mostrarTodos()
    # b = cargoUsuario
    # json_obj = json.loads(result)
    ob = json.dumps(result)
    result3 = json.dumps(mostrarTodosAlunos())
    result2 = json.dumps(mostrarSalas())
    ob2 = json.loads(result2)
    turmasp2 = []
    turmasm2 = []
    alunos_m2 = []
    alunos_p2 = []
    time = []
    ob3 = json.dumps(mostrarTodos_times())
    ob3 = json.loads(ob3)
    ob4 = json.dumps(mostrarTodosAlunos())
    ob4 = json.loads(ob4)

    alunos_turma = []
    alunos_turma2 = []
    alunos = []

    if session['tipo'] == "ALUNO":

        # area q testa pro aluno
        for pos in range(len(ob4)):
            if ob4[pos]['nome'] in session['usuario_logado']:  # se o nome do p2 que eu estou iterando dentro de OB2 (lista de salas) for igual ao do usuário logado
                time.append(ob4[pos]['time'])

            pos += 1
        for x in range(len(ob4)):
            if ob4[x]['time'] in time:
               check = 'ALUNO'
            # for i in range(len(ob4)):
               if check in ob4[x]['cargo']:
                    print('há')
                    print('é o ',ob4[x]['usuario'])
                    alunos.append(ob4[x]['nome'])

            x += 1
        session['meu_time'] = alunos
        print(alunos)

        return render_template("avaliacao.html", result3=result3, alunos=alunos, time=time, perguntas=perguntas)
 

    if session['tipo'] == "PROFESSOR":

        # area q testa pro P2

        for pos in range(len(ob2)):
            if ob2[pos]['p2'] in session['usuario_logado']:  # se o nome do p2 que Feu estou iterando dentro de OB2 (lista de salas) for igual ao do usuário logado
                turmasp2.append(ob2[pos]['sala'])

            pos += 1
        print(turmasp2)
        for x in range(len(ob4)):
            if ob4[x]['sala'] in turmasp2:
               check = 'PRODUCT OWNER (P.O)'
            # for i in range(len(ob4)):
               if check in ob4[x]['funcao']:
                    print('há')
                    print('é o ',ob4[x]['usuario'])
                    alunos_turma.append(ob4[x]['nome'])
            x += 1
        for pos in range(len(ob2)):
            if ob2[pos]['m2'] in session['usuario_logado']:  # se o nome do p2 que eu estou iterando dentro de OB2 (lista de salas) for igual ao do usuário logado
                turmasm2.append(ob2[pos]['sala'])

            pos += 1
        print(turmasm2)
        for x in range(len(ob4)):
            if ob4[x]['sala'] in turmasm2:
               check = 'SCRUM MASTER'
            # for i in range(len(ob4)):
               if check in ob4[x]['funcao']:
                    print('há')
                    print('é o ',ob4[x]['usuario'])
                    alunos_turma2.append(ob4[x]['nome'])

            x += 1
        todos = alunos_turma2+alunos_turma
        session['minha_classe'] = todos
        
        # print(alunos_turma2)
        # print(alunos_turma)
        print('todos da classe',todos,session['minha_classe'])

        return render_template('tela_professor_turmas.html', alunos_turma=alunos_turma,alunos_turma2=alunos_turma2, result=result, perguntas=perguntas)
    return render_template("avaliacao.html", result=result, perguntas=perguntas)

#Notas Alunos

@app.route("/aluno/notas",methods=['POST'])
def aluno_notas():
        lista = [1,2,3,4,5] #lista so pra percorrer a quantidade de perguntas q tem
        option = []
        option2 = []
        resposta2 = []
        resposta = []
        if session['tipo'] == 'ALUNO':
            for i in session['meu_time']:
                option.append(i)
                resposta.clear()
                for x in lista:
                    
                    resposta.append(request.form[i+str(x)])
                    print(request.form[i+str(x)])
                avaliado = Avaliacao(i,resposta,session['usuario_logado'],session['sprint_atual'],'XX/XX/XX','XX/XX/XX')
                inserir2(avaliado)
                
            

            
            result = mostrarTodos2()
            print(resposta)
            
            return redirect("/aluno/avaliacao")
        
        if session['tipo'] == 'PROFESSOR':
            for i in session['minha_classe']:
                option2.append(i)
                resposta2.clear()
                for x in lista:
                    resposta2.append(request.form[i+str(x)])
                    print(request.form[i+str(x)])
                avaliado = Avaliacao(i,resposta2,session['usuario_logado'],session['sprint_atual'],'XX/XX/XX','XX/XX/XX')
                inserir2(avaliado)
                
            

            
            result = mostrarTodos2()
            print(resposta)
            return redirect("/aluno/avaliacao")


# Tela de professores

@app.route('/dashboard', methods=["POST","GET"])
def dash():
    nota = mostrarTodos2()
    return render_template("dashboard.html",nota=nota)

#Admin cadastro times
    
@app.route('/admin/cadastro/times')
def cadastrotimes():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos_times()
    turmas = mostrarSalas()
    return render_template("admin_times.html",
    result=result,turmas=turmas)

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

@app.route('/atualizar/time/<string:id>',methods=["POST","GET"])
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
        turmas = mostrarSalas()
        time = buscarPorIdTime(id)
        return render_template('update_time.html',time = time,turmas=turmas)

#Deletar times do banco de dados

@app.route('/deletar/time/<string:id>')
def deletarTimes(id):
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
    result3 = mostrarTodosAlunos()
    result2 = mostrarTodos_times()
    return render_template("admin_aluno.html",
    result3=result3, result2=result2)

#Inserção alunos no Banco de dados

@app.route('/admin/cadastro/cadastraralunos', methods=["POST","GET"])
def cadastrar_alunos():
    myid = uuid.uuid1()
    id = str(myid)
    obj = json.dumps(mostrarTodos_times())
    obj = json.loads(obj)
    cargo_aluno = request.form["cargo_aluno"]
    nome_aluno = request.form["nome_aluno"]
    usuario_aluno = request.form["usuario_aluno"]
    senha_aluno = request.form["senha_aluno"]
    funcao_aluno = request.form["funcao_aluno"]
    time_aluno = request.form["time_aluno"]
    for x in range(len(obj)):
        if obj[x]['nome_time'] == time_aluno:
            sala_aluno = obj[x]['turma']
            aluno = Alunos(id, cargo_aluno, nome_aluno, usuario_aluno, senha_aluno, funcao_aluno, time_aluno,sala_aluno)
            inserirAlunos(aluno)

    return redirect("/admin/cadastro/alunos")

#Atualizar dados alunos

@app.route('/atualizar/aluno/<string:id>',methods=["POST","GET"])
def atualizar_alunos(id):
    if request.method =='POST':
        id = id
        obj = json.dumps(mostrarTodos_times())
        obj = json.loads(obj)
        cargo_aluno = request.form['cargo']
        nome_aluno = request.form["nome"]
        usuario_aluno = request.form["usuario"]
        senha_aluno = request.form["senha"]
        funcao_aluno = request.form["funcao_aluno"]
        time_aluno = request.form['time']
        for x in range(len(obj)):
            if obj[x]['nome_time'] == time_aluno:
                sala_aluno = obj[x]['turma']
                aluno = Alunos(id, cargo_aluno, nome_aluno, usuario_aluno, senha_aluno, funcao_aluno, time_aluno,
                               sala_aluno)
                inserirAlunos(aluno)
        try:
            atualizarAlunos(id,aluno)
            return redirect('/admin/cadastro/alunos')
        except:
            return 'algo deu errado'
    else:
        result2 = mostrarTodos_times()
        pessoa = buscarPorIdAluno(id)
        return render_template('update_aluno.html',pessoa = pessoa, result2=result2)

#Deletar alunos do banco de dados

@app.route('/deletar/aluno/<string:id>')
def deletarAluno(id):
    try:
        deletarAlunos(id)
        return redirect("/admin/cadastro/alunos")
    except:
        return "Algo de errado aconteceu"
