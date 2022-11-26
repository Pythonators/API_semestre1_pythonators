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

def buscarPorNomeSala(sala):
    return bd.search(n_sala.sala==str(sala))

def atualizarSala(sala: int, model:Salas):
    if bd.search(n_sala.sala==str(sala)):
        bd.remove(n_sala.sala==str(sala))
        inserirSala(model)
    else:
        print("Esse usuário não existe")
def deletarSala(sala: int):
    if bd.search(n_sala.sala==str(sala)):
        bd.remove(n_sala.sala==str(sala))
    else:
        print("Usuário não encontrado")