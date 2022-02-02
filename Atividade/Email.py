from Mensagem import Mensagem


class Email(Mensagem):
    def __init__(self, conteudo, endereco):
        super().__init__(conteudo)
        self._endereco = endereco

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    def __str__(self):
        return "Mensagem enviada para o Email: {}".format(self._endereco)
