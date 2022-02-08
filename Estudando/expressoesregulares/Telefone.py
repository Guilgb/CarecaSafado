import re


class Telefone:
    def __init__(self, telefone):
        if self.validar:
            self.numero = telefone
        else:
            raise ValueError("Numero invállido")

    def validar(self, telefone):
        padrao = "([0-9]{2})([0-9]{2})([0-9]{4})([0-9]{4})"
        resposta = re.search(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def fomat(self):
        padrao = "([0-9]{2})([0-9]{2})([0-9])([0-9]{4})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = (f"+{resposta.group(1)} ({resposta.group(2)})"
                            f"{resposta.group(3)}"
                            f"{resposta.group(4)}-{resposta.group(5)}")
        return (numero_formatado)

    def __str__(self):
        return self.fomat()
