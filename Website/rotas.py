from flask import Flask, render_template, request, redirect, json
from connect import mostrarTodos, inserir, atualizarPessoa, buscarPorId, deletarPessoa, bd
from connectAvaliacao import mostrarTodos2, inserir2
from connectSala import mostrarSalas, inserirSala
from modelos import Usuario, Avaliacao, Salas
from tinydb import TinyDB, Query

app = Flask(__name__)

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
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    result = json.dumps(mostrarTodos())
    lista = json.loads(result)
    cont=0
    if usuario=='admin' and senha=='adm':
        return redirect('/admin')
    else:
        for c in lista:
                cont+=1
                if usuario == c['usuario'] and senha == c['senha']:
                    global nomeUsuario
                    nomeUsuario=c['usuario']
                    global cargoUsuario
                    cargoUsuario = c['cargo']
                    return redirect('/sprint')
                if cont >= len(lista):
                    return redirect("/")
    

@app.route('/sprint', methods = ['GET','POST'])
def pagina_sprint():
    a = nomeUsuario
    return render_template("sprint.html",a=a)

@app.route('/admin')
def pagina_admin():
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin_cadastro.html",
    result=result,salas=salas)

@app.route('/admin/<int:sala>')
def index(sala):
    result = mostrarTodos()
    salas = mostrarSalas()
    return render_template("admin.html",
    result=result, salas=salas)

@app.route('/addSalas', methods=["POST","GET"])
def addSalas():
    sala = request.form["sala"]
    TinyDB(f'Salas/{sala}.json')
    n_sala = Salas(sala)
    inserirSala(n_sala)
    return redirect("/admin/<int:sala>")

@app.route('/admin/cadastrar', methods=["POST","GET"])
def cadastrar():
    id = request.form["id"]
    cargo = request.form["cargo"]
    nome = request.form["nome"]
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    funcao = request.form["funcao"]
    time = request.form["time"]
    pessoa = Usuario(id,cargo,nome,usuario,senha,funcao,time)
    inserir(pessoa)
    return redirect("/admin")

@app.route('/atualizar/<int:id>',methods=["POST","GET"])
def atualizar(id):    
    if request.method =='POST':
        id = request.form["id"]
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

@app.route('/deletar/<int:id>')
def deletar(id):
    try:
        deletarPessoa(id)
        return redirect("/admin")
    except:
        return "Algo de errado aconteceu"



@app.route("/aluno/avaliacao",)
def avaliacao():
    result = mostrarTodos()
    b = cargoUsuario
    #json_obj = json.loads(result)
    ob = json.dumps(result)
    json_obj = json.loads(ob)
    return render_template("avaliacao.html", result = result, perguntas = perguntas,b=b)


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


@app.route('/professor-m2')
def professorm2():
    return "<h1>página professor M2</h1>"

@app.route('/professor-p2')
def professorp2():
    return "<h1>página professor P2</h1>"

@app.route("/professor/dashboard")
def professor_dash():
    return "<h1>página dashboard</h1>"



