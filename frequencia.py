class Frequencia:
    def __init__(self, id_frequencia, data_aula, status, aluno, professor, disciplina):
        self.id_frequencia = id_frequencia
        self.data_aula = data_aula
        self.status = status
        self.aluno = aluno
        self.professor = professor
        self.disciplina = disciplina

        aluno.frequencias.append(self)
