from modelos import Salas
from tinydb import TinyDB, Query
bd = TinyDB("Salas.json")
n_sala = Query()

def inserirSala(model: Salas):
        bd = TinyDB("Salas.json")
        bd.insert({"sala":model.sala, "p2": model.prof,
                   "m2": model.prof2
                   })

def mostrarSalas():
    todos = bd.all()
    return todos

def buscarPorNome(sala_atual):
    return bd.search(n_sala.sala_atual==str(sala_atual))
