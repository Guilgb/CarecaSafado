from Mensagem import Mensagem


class Sms(Mensagem):
    def __init__(self, conteudo, telefone):
        super().__init__(conteudo)
        self._telefone = telefone

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    def __str__(self):
        return "Mensagem enviada para o número: {}".format(self._telefone)
