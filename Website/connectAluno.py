from modelos import Alunos
from tinydb import TinyDB, Query
import pandas as pd

bdAlunos = TinyDB("Alunos.json")
aluno = Query()
def inserirAlunos(model: Alunos):
    bdAlunos.insert({"id":model.id,
    "cargo":model.cargo,
    "nome":model.nome,
    "usuario":model.usuario,
    "senha":model.senha,
    "funcao":model.funcao,
    "time":model.time,
    "sala": model.sala})
def mostrarTodosAlunos():
    todos = bdAlunos.all()
    return todos
def atualizarAlunos(id: int, model:Alunos):
    if bdAlunos.search(aluno.id==str(id)):
        bdAlunos.remove(aluno.id==str(id))
        inserirAlunos(model)
    else:
        print("Esse usuário não existe")
def buscarPorIdAluno(id):
    return bdAlunos.search(aluno.id==str(id))
def deletarAlunos(id: int):
    if bdAlunos.search(aluno.id==str(id)):
        bdAlunos.remove(aluno.id==str(id))
    else:
        print("Usuário não encontrado")
