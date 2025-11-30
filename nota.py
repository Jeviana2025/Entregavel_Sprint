from datetime import date

class Nota:
    def __init__(self, id_nota, aluno, disciplina, valor, tipo_avaliacao):
        self.id_nota = id_nota
        self.aluno = aluno
        self.disciplina = disciplina
        self.valor = valor
        self.tipo_avaliacao = tipo_avaliacao
        self.data_registro = date.today()

    def __repr__(self):
        return f"<Nota {self.valor} - {self.aluno.nome} ({self.disciplina.nome})>"
