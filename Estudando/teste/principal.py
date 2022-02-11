from dominio import Usuario, Lance, Leilao, Avaliador


gui = Usuario("Guilherme")
camyla = Usuario("Camyla")
gael = Usuario("Gael")

lance_gui = Lance(gui, 100)
lance_camy = Lance(camyla, 200)
lance_gael = Lance(gael, 20)

leilao = Leilao("Lance de Celulares")
leilao.lances.append(lance_gui)
leilao.lances.append(lance_camy)
leilao.lances.append(lance_gael)

for lance in leilao.lances:
    print(
        f"Usuario: {lance.usuario.nome}\nLance: {lance.valor}\n"
        f"--------------------"
    )

avaliador = Avaliador()
avaliador.avalia(leilao)
print(
    f"O menor lance foi de: {avaliador.menor_lance} \n"
    f"O maior lance foi de: {avaliador.maior_lance}"
)
