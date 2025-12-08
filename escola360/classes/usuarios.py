# implementar os usuários do Sistema Escola 360
# Interfaces: Autenticavel.
# Classe base: Usuario.
#Subclasses: Gestor, Professor, Responsavel.

from abc import ABC, abstractmethod
from datetime import date
from typing import List

# ====================== INTERFACE ======================

class Autenticavel(ABC):
    @abstractmethod
    def fazer_login(self, email: str, senha: str) -> bool:
        """Verifica se credenciais são válidas."""
        raise NotImplementedError

class GeradorRelatorio(ABC):
    @abstractmethod
    def gerar_relatorio(self) -> "Relatorio":
        raise NotImplementedError
        
# ====================== CLASSE BASE ======================

class Usuario(Autenticavel, ABC):
    def __init__(self, id_usuario: int, email: str, senha: str, cpf: str, telefone: str, endereco: str):
        self.__id_usuario = id_usuario
        self.__email = email
        self.__senha = senha
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco

# -------- getters / setters -------

    @property
    def id_usuario(self) -> int:
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, value: int) -> None:
        if value <= 0:
            raise ValueError("id_usuario deve ser positivo")
        self.__id_usuario = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        if "@" not in value:
            raise ValueError("email inválido")
        self.__email = value

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, value: str) -> None:
        if not value:
            raise ValueError("cpf não pode ser vazio")
        self.__cpf = value

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, value: str) -> None:
        self.__telefone = value

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, value: str) -> None:
        self.__endereco = value

   # --- operações de usuário ---

    def fazer_login(self, email: str, senha: str) -> bool:
        return self.__email == email and self.__senha == senha

    def criar(self) -> None:
        print(f"[USUARIO] criando usuário {self.__id_usuario}")

    def ler(self) -> dict:
        return {
            "id": self.__id_usuario,
            "email": self.__email,
            "cpf": self.__cpf,
            "telefone": self.__telefone,
            "endereco": self.__endereco,
        }

    def atualizar(self, **dados) -> None:
        for campo, valor in dados.items():
            if hasattr(self.__class__, campo):
                setattr(self, campo, valor)

    def excluir(self) -> None:
        print(f"[USUARIO] excluindo usuário {self.__id_usuario}")


# ====================== SUBTIPOS DE USUARIO =========
# Nesta face serão implementadas as subclasses.
#class Gestor(Usuario)
#class Professor(Usuario)
#class Responsavel(Usuario)

from datetime import date

# ====================== GESTOR ======================

class Gestor(Usuario, GeradorRelatorio):
    def __init__(self, id_usuario: int, email: str, senha: str,
                 cpf: str, telefone: str, endereco: str,
                 id_gestor: int, nome: str, cargo: str):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__id_gestor = id_gestor
        self.__nome = nome
        self.__cargo = cargo
        self.__relatorios: List["Relatorio"] = []

    @property
    def id_gestor(self) -> int:
        return self.__id_gestor

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cargo(self) -> str:
        return self.__cargo

    @property
    def relatorios(self) -> List["Relatorio"]:
        return list(self.__relatorios)

    def gerar_relatorio(self) -> "Relatorio":
        from .relatorios import Relatorio  # import local para baixo acoplamento
        relatorio = Relatorio(
            id_relatorio=len(self.__relatorios) + 1,
            nome_relatorio=f"Relatório do gestor {self.__nome}",
            data_geracao=date.today(),
        )
        self.__relatorios.append(relatorio)
        return relatorio


# ====================== PROFESSOR ======================

class Professor(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str,
                 cpf: str, telefone: str, endereco: str,
                 id_professor: int, nome: str, data_nascimento: date):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__id_professor = id_professor
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__frequencias: List["Frequencia"] = []
        self.__notas_lancadas: List["Nota"] = []

    @property
    def id_professor(self) -> int:
        return self.__id_professor

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def frequencias(self) -> List["Frequencia"]:
        return list(self.__frequencias)

    @property
    def notas_lancadas(self) -> List["Nota"]:
        return list(self.__notas_lancadas)

    def lancar_nota(self, aluno: "Aluno", disciplina: "Disciplina",
                    data_avaliacao: date, tipo_avaliacao: str,
                    valor: float) -> "Nota":
        from .avaliacao import Nota
        from .disciplinas import Disciplina
        if not (0.0 <= valor <= 10.0):
            raise ValueError("valor da nota deve estar entre 0 e 10")
        nota = Nota(
            id_nota=len(self.__notas_lancadas) + 1,
            data_avaliacao=data_avaliacao,
            tipo_avaliacao=tipo_avaliacao,
            valor=valor,
            aluno=aluno,
            disciplina=disciplina,
        )
        self.__notas_lancadas.append(nota)
        aluno._Aluno__adicionar_nota(nota)
        disciplina._Disciplina__adicionar_nota(nota)
        return nota

    def registrar_frequencia(self, aluno: "Aluno", disciplina: "Disciplina",
                             data_aula: date, presente: bool) -> "Frequencia":
        from .avaliacao import Frequencia
        from .disciplinas import Disciplina
        freq = Frequencia(
            id_frequencia=len(self.__frequencias) + 1,
            data_aula=data_aula,
            status_frequencia="P" if presente else "F",
            professor=self,
            aluno=aluno,
            disciplina=disciplina,
        )
        self.__frequencias.append(freq)
        aluno._Aluno__adicionar_frequencia(freq)
        disciplina._Disciplina__adicionar_frequencia(freq)
        return freq

'''
# ====================== ALUNO ======================

class Aluno(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str, cpf: str, telefone: str,
                 endereco: str, matricula: str, data_nascimento: date, serie: str):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__matricula = matricula
        self.__data_nascimento = data_nascimento
        self.__serie = serie

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, value: str) -> None:
        if not value:
            raise ValueError("matricula inválida")
        self.__matricula = value

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value: date) -> None:
        self.__data_nascimento = value

    @property
    def serie(self) -> str:
        return self.__serie

    @serie.setter
    def serie(self, value: str) -> None:
        self.__serie = value

    def visualizar_boletim(self):
        print(f"[ALUNO] Exibindo boletim do aluno {self.matricula}")

'''
# ====================== RESPONSÁVEL ======================

class Responsavel(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str,
                 cpf: str, telefone: str, endereco: str,
                 id_responsavel: int, nome: str):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__id_responsavel = id_responsavel
        self.__nome = nome
        self.__alunos: List["Aluno"] = []

    @property
    def id_responsavel(self) -> int:
        return self.__id_responsavel

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def alunos(self) -> List["Aluno"]:
        return list(self.__alunos)

    def adicionar_aluno(self, aluno: "Aluno") -> None:
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)
            aluno._Aluno__adicionar_responsavel(self)






