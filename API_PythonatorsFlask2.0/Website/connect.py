from modelos import Usuario
from tinydb import TinyDB, Query
import pandas as pd

bd = TinyDB("Pessoas.json")
usuario = Query()
def inserir(model: Usuario):
    '''Insere um modelo no banco de dados'''
    bd.insert({"id":model.id,
    "cargo":model.cargo,
    "nome":model.nome,
    "usuario":model.usuario,
    "senha":model.senha,
    "funcao":model.funcao,
    "time":model.time})
def mostrarTodos():
    '''Mostra todos os contatos cadastrados no banco de dados'''
    todos = bd.all()
    return todos

