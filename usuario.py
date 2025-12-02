# implementar os usuários do Sistema Escola 360
# Interfaces: Autenticavel.
# Classe base: Usuario.
#Subclasses: Gestor, Professor, Aluno, Responsavel.

from abc import ABC, abstractmethod
from datetime import date

# ====================== INTERFACE ======================

class Autenticavel(ABC):
    @abstractmethod
    def fazer_login(self, email: str, senha: str) -> bool:
        """Verifica se credenciais são válidas."""
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

# -------- getters / setters (encapsulamento forte) -------

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
#class Aluno(Usuario)
#class Responsavel(Usuario)

from datetime import date

# ====================== GESTOR ======================

class Gestor(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str, cpf: str, telefone: str, 
                 endereco: str, cargo: str):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__cargo = cargo

    @property
    def cargo(self) -> str:
        return self.__cargo

    @cargo.setter
    def cargo(self, value: str) -> None:
        if not value:
            raise ValueError("cargo não pode ser vazio")
        self.__cargo = value

    def gerar_relatorio_escolar(self):
        print(f"[GESTOR] Gerando relatório escolar...")


# ====================== PROFESSOR ======================

class Professor(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str, cpf: str, telefone: str,
                 endereco: str, disciplina: str, matricula: str):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__disciplina = disciplina
        self.__matricula = matricula

    @property
    def disciplina(self) -> str:
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, value: str) -> None:
        if not value:
            raise ValueError("disciplina não pode ser vazia")
        self.__disciplina = value

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, value: str) -> None:
        if not value:
            raise ValueError("matricula inválida")
        self.__matricula = value

    def lancar_nota(self, aluno_id: int, nota: float):
        print(f"[PROFESSOR] Nota {nota} lançada para o aluno {aluno_id}")

    def registrar_frequencia(self, aluno_id: int, presente: bool):
        status = "Presente" if presente else "Faltou"
        print(f"[PROFESSOR] Frequência: {status} para o aluno {aluno_id}")


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


# ====================== RESPONSÁVEL ======================

class Responsavel(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str, cpf: str, telefone: str,
                 endereco: str, nome_responsavel: str, aluno_vinculado: Aluno):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__nome_responsavel = nome_responsavel
        self.__aluno_vinculado = aluno_vinculado

    @property
    def nome_responsavel(self) -> str:
        return self.__nome_responsavel

    @nome_responsavel.setter
    def nome_responsavel(self, value: str) -> None:
        if not value:
            raise ValueError("nome_responsavel inválido")
        self.__nome_responsavel = value

    @property
    def aluno_vinculado(self) -> Aluno:
        return self.__aluno_vinculado

    @aluno_vinculado.setter
    def aluno_vinculado(self, value: Aluno) -> None:
        self.__aluno_vinculado = value

    def acompanhar_desempenho(self):
        print(f"[RESPONSÁVEL] Acompanhando desempenho do aluno {self.__aluno_vinculado.matricula}")






