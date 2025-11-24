from src.usuario import Usuario
from src.relatorio import Relatorio

class Gestor(Usuario):
    def __init__(self, id_usuario, nome, email, senha, cargo):
        super().__init__(id_usuario, nome, email, senha)
        self.cargo = cargo

    def gerar_relatorio(self, nome_relatorio, alunos, notas, frequencias):
        relatorio = Relatorio(nome_relatorio, alunos, notas, frequencias)
        print(f"Relatório '{nome_relatorio}' gerado por {self.nome}.")
        return relatorio
