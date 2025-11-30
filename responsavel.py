from usuario import Usuario

class Responsavel(Usuario):
    def __init__(self, id_usuario, nome, email, senha, cpf, telefone):
        super().__init__(id_usuario, nome, email, senha, cpf, telefone)

    def gerar_relatorio(self, relatorio):
        print(f"Responsável {self.nome} gerou o relatório {relatorio.nome_relatorio}")

