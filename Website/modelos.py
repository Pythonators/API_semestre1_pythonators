class Professor:
    def __init__(self, id, nome, usuario, senha) -> None:
        self.id=id
        self.nome=nome
        self.usuario=usuario
        self.senha=senha
        #self.funcao=funcao
class Avaliacao:
    def __init__(self, avaliado, perguntas,avaliador,sprint,data_inicio,data_fim) -> None:
        self.avaliado=avaliado
        self.perguntas = perguntas
        self.avaliador = avaliador
        self.sprint = sprint
        self.data_inicio = data_inicio
        self.data_fim = data_fim
class Salas:
    def __init__(self, sala,prof,prof2):
        self.sala = sala
        self.prof = prof
        self.prof2 = prof2
class Sprint:
    def __init__(self,sprint,data):
        self.sprint=sprint
        self.data=data
class Times:
    def __init__(self,id,turma,nome_time):
        self.id=id
        self.turma=turma
        self.nome_time=nome_time
class Alunos:
    def __init__(self, id, cargo, nome, usuario, senha, funcao, time,sala) -> None:
        self.id=id
        self.cargo=cargo
        self.nome=nome
        self.usuario=usuario
        self.senha=senha
        self.funcao=funcao
        self.time=time
        self.sala=sala