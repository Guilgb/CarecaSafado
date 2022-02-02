from abc import abstractmethod


@abstractmethod
class Mensagem:
    def __init__(self, conteudo):
        self._conteudo = conteudo

    @property
    def conteudo(self):
        return self._conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo

    def __str__(self):
        return ""
