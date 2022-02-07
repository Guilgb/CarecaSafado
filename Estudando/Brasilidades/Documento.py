import DocCpf
import DocCnpj


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
