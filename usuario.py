class Usuario:
    def __init__(self, id_usuario, nome, email, senha, cpf, telefone):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone

    def fazer_login(self, email, senha):
        return self.email == email and self.senha == senha

    def criar(self):
        print(f"Usuário {self.nome} criado no sistema.")

    def ler(self):
        return vars(self)

    def atualizar(self, **kwargs):
        for chave, valor in kwargs.items():
            setattr(self, chave, valor)

    def excluir(self):
        print(f"Usuário {self.nome} removido do sistema.")

