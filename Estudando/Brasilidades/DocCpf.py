from validate_docbr import CPF


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf Indvalido")

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def fortmat(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.fortmat()
