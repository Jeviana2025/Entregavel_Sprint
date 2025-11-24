class Disciplina:
    def __init__(self, id_disciplina, nome):
        self.id_disciplina = id_disciplina
        self.nome = nome
        self.notas = []
        self.frequencias = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def adicionar_frequencia(self, freq):
        self.frequencias.append(freq)
