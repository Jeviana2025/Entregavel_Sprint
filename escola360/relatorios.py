#Implementa a Classe Relatorio.
#Define os métodos e atributos da Classe Relatorio.

from __future__ import annotations
from datetime import date

class Relatorio:
    """
    Classe simples para o objeto Relatorio, usado principalmente pela classe Gestor.
    Representa um documento gerado com informações específicas do sistema.
    """
    def __init__(self, id_relatorio: int, nome_relatorio: str,
                 data_geracao: date):
        # Atributos privados para encapsulamento
        self.__id_relatorio = id_relatorio
        self.__nome_relatorio = nome_relatorio
        self.__data_geracao = data_geracao

    # Properties de leitura (getters)

    @property
    def id_relatorio(self) -> int:
        return self.__id_relatorio

    @property
    def nome_relatorio(self) -> str:
        return self.__nome_relatorio

    @property
    def data_geracao(self) -> date:
        return self.__data_geracao

    def adicionar_informacoes(self, texto: str) -> None:
        """
        Método de demonstração para adicionar conteúdo ao relatório (via print).
        Em um sistema real, este método adicionaria texto a um buffer/arquivo.
        """
        print(f"[RELATORIO {self.__id_relatorio}] {texto}")
