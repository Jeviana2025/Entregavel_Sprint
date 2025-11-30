from usuario import Usuario

class Professor(Usuario):
    def __init__(self, id_usuario, nome, email, senha, cpf, telefone):
        super().__init__(id_usuario, nome, email, senha, cpf, telefone)

    def lancar_nota(self, nota):
        print(f"Professor {self.nome} lançou a nota {nota.valor} para o aluno {nota.aluno.nome}")

    def registrar_frequencia(self, frequencia):
        print(f"Professor {self.nome} registrou frequência de {frequencia.status} para o aluno {frequencia.aluno.nome}")
        
