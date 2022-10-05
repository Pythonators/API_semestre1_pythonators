from modelos import Usuario
from tinydb import TinyDB, Query
import pandas as pd

bd = TinyDB("Pessoas.json")
usuario = Query()
def inserir(model: Usuario):
    bd.insert({"id":model.id,
    "cargo":model.cargo,
    "nome":model.nome,
    "usuario":model.usuario,
    "senha":model.senha,
    "funcao":model.funcao,
    "time":model.time})
def mostrarTodos():
    todos = bd.all()
    return todos

def atualizarPessoa(id: int, model:Usuario):
    if bd.search(usuario.id==str(id)):
        bd.remove(usuario.id==str(id))
        inserir(model)
    else:
        print("Esse usuário não existe")
def buscarPorId(id):
    return bd.search(usuario.id==str(id))
def deletarPessoa(id: int):
    if bd.search(usuario.id==str(id)):
        bd.remove(usuario.id==str(id))
    else:
        print("Usuário não encontrado")