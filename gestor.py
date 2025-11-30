from usuario import Usuario

class Gestor(Usuario):
    def __init__(self, id_usuario, nome, email, senha, cpf, telefone, cargo):
        super().__init__(id_usuario, nome, email, senha, cpf, telefone)
        self.cargo = cargo

    def gerar_relatorio(self, relatorio):
        print(f"Gestor {self.nome} gerou o relatório {relatorio.nome_relatorio}")

