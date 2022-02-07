import re


class Telefone:
    def __init__(self, telefone):
        if self.validar:
            self.numero = telefone
        else:
            raise ValueError("Numero invállido")

    def validar(self, telefone):
        padrao = "[0-9]{2}[0-9]{4, 5}[0-9]{4}"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def __str__(self):
        pass
