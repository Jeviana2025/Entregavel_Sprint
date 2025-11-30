class Nota:
    def __init__(self, id_nota, valor, data, tipo_avaliacao, aluno, professor, disciplina):
        self.id_nota = id_nota
        self.valor = valor
        self.data = data
        self.tipo_avaliacao = tipo_avaliacao
        self.aluno = aluno
        self.professor = professor
        self.disciplina = disciplina

        aluno.notas.append(self)

