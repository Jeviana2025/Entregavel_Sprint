class Usuario:
    def __init__(self, id_usuario, nome, email, senha, cpf=None, telefone=None, endereco=None):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

    def fazer_login(self, email, senha):
        return self.email == email and self.senha == senha

    def criar(self):
        print(f"Usuário {self.nome} criado.")

    def ler(self):
        print(f"Usuário: {self.nome}, Email: {self.email}")

    def atualizar(self):
        print(f"Usuário {self.nome} atualizado.")

    def excluir(self):
        print(f"Usuário {self.nome} excluído.")
