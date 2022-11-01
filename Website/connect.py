from modelos import Professor
from tinydb import TinyDB, Query
import pandas as pd

bdProfessor = TinyDB("Professor.json")
professor = Query()
def inserir(model: Professor):
    bdProfessor.insert({"id":model.id,
    "cargo":model.cargo,
    "nome":model.nome,
    "usuario":model.usuario,
    "senha":model.senha,
    "funcao":model.funcao})
def mostrarTodos():
    todos = bdProfessor.all()
    return todos
def atualizarProfessor(id: int, model:Professor):
    if bdProfessor.search(professor.id==str(id)):
        bdProfessor.remove(professor.id==str(id))
        inserir(model)
    else:
        print("Esse usuário não existe")
def buscarPorId(id):
    return bdProfessor.search(professor.id==str(id))
def deletarProfessor(id: int):
    if bdProfessor.search(professor.id==str(id)):
        bdProfessor.remove(professor.id==str(id))
    else:
        print("Usuário não encontrado")