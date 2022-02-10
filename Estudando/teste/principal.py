from dominio import Usuario
from dominio import Lance
from dominio import Leilao


gui = Usuario("Guilherme")
camyla = Usuario("Camyla")

lance_gui = Lance(gui, 190)
lance_camy = Lance(camyla, 200)

leilao = Leilao("Lance de Celulares")
leilao.lances.append(lance_gui)
leilao.lances.append(lance_camy)

for lance in leilao.lances:
    print(
        f"Usuario: {lance.usuario.nome}\nLance: {lance.valor}\n"
        f"--------------------"
    )
