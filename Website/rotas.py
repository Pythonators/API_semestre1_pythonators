from flask import Flask, flash, render_template, request, redirect, json, session
from connect import mostrarTodos, inserir, atualizarPessoa, buscarPorId, deletarPessoa, bd
from connectAvaliacao import mostrarTodos2, inserir2
from connectSala import mostrarSalas, inserirSala
from modelos import Usuario, Avaliacao, Salas
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

@app.route('/', methods = ['GET','POST'])
def pagina_login():
    return render_template("index.html")

@app.route('/autenticar', methods = ['GET','POST'])
def autenticar():
    Q = Query()
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    result = json.dumps(mostrarTodos())
    
    if usuario == 'admin' and senha == '1234':
        session['adminlogado'] = "admin"
        return redirect("/admin")
    if bd.search(Q.usuario == usuario) and bd.search(Q.senha == senha):
        session["usuario_logado"] = request.form['nome']
        return redirect('/sprint')
    else:
         return redirect("/")
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    session['adminlogado'] = None
    return redirect('/')

@app.route('/sprint', methods = ['GET','POST'])
def pagina_sprint():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    return render_template("sprint.html")

@app.route('/admin')
def pagina_admin():
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin_cadastro.html",
    result=result,salas=salas)

@app.route('/admin/<string:sala>')
def index(sala):
    if 'usuario_logado' in session:
        redirect("/")
    if 'adminlogado' not in session or session['adminlogado'] == None:
        return redirect('/')
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin.html",
    result=result, salas=salas)

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
    return redirect("/admin/<string:sala>")

@app.route('/admin/cadastrar', methods=["POST","GET"])
def cadastrar():
    myid = uuid.uuid1()
    id = str(myid)
    cargo = request.form["cargo"]
    nome = request.form["nome"]
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    funcao = request.form["funcao"]
    time = request.form["time"]
    pessoa = Usuario(id,cargo,nome,usuario,senha,funcao,time)
    inserir(pessoa)
    return redirect("/admin")

@app.route('/atualizar/<string:id>',methods=["POST","GET"])
def atualizar(id):
    if request.method =='POST':
        id = id
        cargo = request.form["cargo"]
        nome = request.form["nome"]
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        funcao = request.form["funcao"]
        time = request.form["time"]
        pessoa = Usuario(id,cargo,nome,usuario,senha,funcao,time)
        try:
            atualizarPessoa(id,pessoa)
            return redirect('/admin')
        except:
            return 'algo deu errado'
    else:
        pessoa = buscarPorId(id)
        return render_template('update.html',pessoa = pessoa)

@app.route('/deletar/<string:id>')
def deletar(id):
    try:
        deletarPessoa(id)
        return redirect("/admin")
    except:
        return "Algo de errado aconteceu"

    #b = cargoUsuario
    #json_obj = json.loads(result)
    ob = json.dumps(result)
    json_obj = json.loads(ob)
    return render_template("avaliacao.html", result = result, perguntas = perguntas)

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


@app.route('/professor')
def professorm2():
    return render_template("tela_do_professor.html")

@app.route("/professor/dashboard")
def professor_dash():
    return "<h1>página dashboard</h1>"

