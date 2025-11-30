class Aluno:
    def __init__(self, id_aluno, nome, data_nascimento):
        self.id_aluno = id_aluno
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.notas = []
        self.frequencias = []
        self.responsaveis = []

    def consultar_notas(self):
        return self.notas

    def consultar_frequencias(self):
        return self.frequencias

    def adicionar_responsavel(self, responsavel):
        self.responsaveis.append(responsavel)
