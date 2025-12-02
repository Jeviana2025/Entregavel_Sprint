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

# ====================== SUBTIPOS DE USUARIO ======================

#Falta implementar



