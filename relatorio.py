from datetime import date

class Relatorio:
    contador = 1

    def __init__(self, nome_relatorio, alunos, notas, frequencias):
        self.id_relatorio = Relatorio.contador
        Relatorio.contador += 1
        self.nome_relatorio = nome_relatorio
        self.data_geracao = date.today()
        self.alunos = alunos
        self.notas = notas
        self.frequencias = frequencias

    def __repr__(self):
        return (f"<Relatório {self.nome_relatorio} | "
                f"Alunos={len(self.alunos)}, Notas={len(self.notas)}, Freq={len(self.frequencias)}>")
