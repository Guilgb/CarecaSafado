from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)

        if self.cpf_validar(documento):
            self.cpf = documento

    def cpf_validar(self, cpf):
        if(len(cpf) == 11):
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()
