from src.usuario import Usuario

class Responsavel(Usuario):
    def __init__(self, id_usuario, nome, email, senha, telefone):
        super().__init__(id_usuario, nome, email, senha, telefone=telefone)
