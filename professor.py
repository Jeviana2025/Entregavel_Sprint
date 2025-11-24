from src.usuario import Usuario
from src.nota import Nota
from src.frequencia import Frequencia
from datetime import date

class Professor(Usuario):
    def __init__(self, id_usuario, nome, email, senha, data_nascimento):
        super().__init__(id_usuario, nome, email, senha)
        self.data_nascimento = data_nascimento
        self.notas = []
        self.frequencias = []

    def lancar_nota(self, id_nota, aluno, disciplina, valor, tipo_avaliacao):
        nota = Nota(id_nota, aluno, disciplina, valor, tipo_avaliacao)
        self.notas.append(nota)
        aluno.adicionar_nota(nota)
        disciplina.adicionar_nota(nota)
        print(f"Nota {valor} lançada para {aluno.nome} em {disciplina.nome}.")
        return nota

    def registrar_frequencia(self, id_frequencia, aluno, disciplina, status):
        freq = Frequencia(id_frequencia, aluno, disciplina, date.today(), status)
        self.frequencias.append(freq)
        aluno.adicionar_frequencia(freq)
        disciplina.adicionar_frequencia(freq)
        print(f"Frequência registrada: {aluno.nome} - {status} ({disciplina.nome})")
        return freq
