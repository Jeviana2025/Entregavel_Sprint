# Implementa a Classe Disciplina

class Disciplina:
    def __init__(self, id_disciplina: int, nome: str):
        self.id_disciplina = id_disciplina
        self.nome = nome
        self._notas: List[Nota] = []
        self._frequencias: List[Frequencia] = []

    def adicionar_nota(self, nota: "Nota"):
        self._notas.append(nota)

    def adicionar_frequencia(self, frequencia: "Frequencia"):
        self._frequencias.append(frequencia)

    def listar_notas(self) -> List["Nota"]:
        return list(self._notas)

    def listar_frequencias(self) -> List["Frequencia"]:
        return list(self._frequencias)
