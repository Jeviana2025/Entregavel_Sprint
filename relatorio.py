class Relatorio:
    def __init__(self, id_relatorio, nome_relatorio, data_geracao, aluno):
        self.id_relatorio = id_relatorio
        self.nome_relatorio = nome_relatorio
        self.data_geracao = data_geracao
        self.aluno = aluno

    def gerar(self):
        print(f"Relatório gerado para o aluno {self.aluno.nome}")
