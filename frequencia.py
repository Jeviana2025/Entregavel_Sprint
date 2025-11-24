class Frequencia:
    def __init__(self, id_frequencia, aluno, disciplina, data, status):
        self.id_frequencia = id_frequencia
        self.aluno = aluno
        self.disciplina = disciplina
        self.data = data
        self.status = status

    def __repr__(self):
        return f"<Freq {self.aluno.nome} - {self.status} ({self.disciplina.nome})>"
