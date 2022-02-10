from lances in leilao.lances:
from dominio import Usuario
from dominio import Lance
from dominio import Leilao


gui = Usuario("Guilherme")
camyla = Usuario("Camyla")

lance_gui = Lance(gui, 190)
lance_camy = Lance(camyla, 200)

leilao = Leilao("Lance de Celulares")
leilao.lances.append(lance_gui)

for lance in leilao.lances:
    print(lance.usuario.nome)
