from validate_docbr import CNPJ
from validate_docbr import CPF


class Documento:
    # @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if(len(documento) == 11):
            return DocCpf(documento)
        elif(len(documento) == 14):
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos esta incorreta")


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


class DocCnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ("CNPJ invalido")

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()


cnpj = "35337983800011"
cpf = "07341965398222"
documento = Documento.cria_documento("35337983800012")
print(documento)
