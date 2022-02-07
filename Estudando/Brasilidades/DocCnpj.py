from validate_docbr import CNPJ


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ("CNPJ invalido")

    def valida(self, documento):
        validador = documento
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask()

    def __str__(self):
        return self.format()
