from tinydb import TinyDB, Query
from modelos import Avaliacao
import pandas as pd

bd = TinyDB("Avaliacao.json")
avaliacao = Query()
def inserir2(model: Avaliacao):
    bd.insert({"avaliado":model.avaliado,
    "perguntas": model.perguntas
   })
def mostrarTodos2():
    todos = bd.all()
    return todos