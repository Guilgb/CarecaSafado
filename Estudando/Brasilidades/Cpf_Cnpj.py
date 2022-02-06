from validate_docbr import CPF
from validate_docbr import CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_docuento = tipo_documento
        documento = str(documento)
        if(tipo_documento == "cpf"):
            if self.cpf_validar(documento):
                self.cpf = documento
            else:
                raise "CPF inválido"
        elif(tipo_documento == "cnpj"):
            if self.validar_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError("Cnpj inválido")
        else:
            raise ValueError("Documento inválido")

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

    def validar_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos invalido")
