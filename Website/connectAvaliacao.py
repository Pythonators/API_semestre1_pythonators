from tinydb import TinyDB, Query
from modelos import Avaliacao
import pandas as pd
import statistics

bd = TinyDB("Avaliacao.json")
avaliacao = Query()
def inserir2(model: Avaliacao):
    bd.insert({"avaliado":model.avaliado,
    "perguntas": statistics.mode(model.perguntas),
    "avaliador": model.avaliador,
    "sprint": model.sprint,
    "data_inicio": model.data_inicio,
    "data_fim": model.data_fim
   })
def mostrarTodos2():
    todos = bd.all()
    return todos