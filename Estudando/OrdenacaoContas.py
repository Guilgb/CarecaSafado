from operator import attrgetter


class Conta:
    def __init__(self, nome, saldo) -> None:
        self.nome = nome
        self._saldo = saldo

    def __it__(self, outro):
        return self._saldo < outro._saldo


conta_guilherme = Conta("Guilherme", 100)
conta_camyla = Conta("Camyla", 200)
conta_gael = Conta("Gael", 500)
conta_manoel = Conta("Manoel", 500)


contas = [conta_guilherme, conta_camyla, conta_gael, conta_manoel]


# Ordena por saldo de cada conta
# attrgetter pega um atributo privado
for conta in sorted(contas, key=attrgetter("_saldo", "nome")):
    print(conta.nome)
