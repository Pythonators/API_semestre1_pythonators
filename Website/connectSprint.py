from modelos import Sprint
from tinydb import TinyDB, Query

bd = TinyDB("SprintDatabase.json")
n_sprint = Query()


def mostrarSprint():
    todos = bd.all()
    return todos


def buscarPorNome(sprint):
    return bd.search(n_sprint.sprint==int(sprint))