from modelos import Times
from tinydb import TinyDB, Query
import pandas as pd

bdtime = TinyDB("Times.json")
time = Query()
def inserir_time(model: Times):
    bdtime.insert({"id":model.id,
    "turma":model.turma,
    "nome_time":model.nome_time })
def mostrarTodos_times() -> object:
    todos = bdtime.all()
    return todos
def atualizarTimes(id: int, model:Times):
    if bdtime.search(time.id==str(id)):
        bdtime.remove(time.id==str(id))
        inserir_time(model)
    else:
        print("Esse usuário não existe")
def buscarPorIdTime(id):
    return bdtime.search(time.id==str(id))
def deletarTime(id: int):
    if bdtime.search(time.id==str(id)):
        bdtime.remove(time.id==str(id))
    else:
        print("Usuário não encontrado")