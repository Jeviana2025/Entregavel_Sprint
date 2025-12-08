#Implementa a Classe Aluno e seus Métodos


from __future__ import annotations
from datetime import date
from typing import List

from .usuarios import Usuario  


class Aluno(Usuario):
    def __init__(self, id_usuario: int, email: str, senha: str,
                 cpf: str, telefone: str, endereco: str,
                 id_aluno: int, nome: str, data_nascimento: date):
        super().__init__(id_usuario, email, senha, cpf, telefone, endereco)
        self.__id_aluno = id_aluno
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__responsaveis: List["Responsavel"] = []
        self.__notas: List["Nota"] = []
        self.__frequencias: List["Frequencia"] = []

    @property
    def id_aluno(self) -> int:
        return self.__id_aluno

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @property
    def responsaveis(self) -> List["Responsavel"]:
        return list(self.__responsaveis)

    @property
    def notas(self) -> List["Nota"]:
        return list(self.__notas)

    @property
    def frequencias(self) -> List["Frequencia"]:
        return list(self.__frequencias)

    def consultar_nota(self) -> List["Nota"]:
        return list(self.__notas)

    def consultar_frequencia(self) -> List["Frequencia"]:
        return list(self.__frequencias)

    # métodos internos usados por Professor/Responsavel

    def __adicionar_responsavel(self, responsavel: "Responsavel") -> None:
        if responsavel not in self.__responsaveis:
            self.__responsaveis.append(responsavel)

    def __adicionar_nota(self, nota: "Nota") -> None:
        self.__notas.append(nota)

    def __adicionar_frequencia(self, frequencia: "Frequencia") -> None:
        self.__frequencias.append(frequencia)


