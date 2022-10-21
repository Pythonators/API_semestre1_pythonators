class Usuario:
    def __init__(self, id, cargo, nome, usuario, senha, funcao, time) -> None:
        self.id=id
        self.cargo = cargo
        self.nome=nome
        self.usuario=usuario
        self.senha=senha
        self.funcao=funcao
        self.time=time
class Avaliacao:
    def __init__(self, avaliado, perguntas) -> None:
        self.avaliado=avaliado
        self.perguntas = perguntas
class Salas:
    def __init__(self, sala):
        self.sala = sala