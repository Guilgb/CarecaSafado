class Cpf:
    def __init__(self, documento):
        documento = str(documento)

        if self.cpf_validar(documento):
            self.cpf = documento

    def cpf_validar(self, documento):
        if(len(documento) == 11):
            return True
        else:
            return False

    def format_cpf(self):
        fatia_cpf = self.cpf[:3]
        fatia_cpf1 = self.cpf[3:6]
        fatia_cpf2 = self.cpf[6:9]
        fatia_cpf3 = self.cpf[9:]
        return f"{fatia_cpf}.{fatia_cpf1}.{fatia_cpf2}-{fatia_cpf3}"

    def __str__(self):
        return self.format_cpf()
