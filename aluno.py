class Aluno:
    def __init__(self, id_aluno, nome, data_nascimento):
        self.id_aluno = id_aluno
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.notas = []
        self.frequencias = []
        self.responsaveis = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def adicionar_frequencia(self, freq):
        self.frequencias.append(freq)

    def consultar_notas(self):
        return [f"{n.disciplina.nome}: {n.valor}" for n in self.notas]

    def consultar_frequencias(self):
        return [f"{f.data} - {f.disciplina.nome}: {f.status}" for f in self.frequencias]

    def adicionar_responsavel(self, responsavel):
        self.responsaveis.append(responsavel)
