from dominio import Usuario, Lance, Leilao


gui = Usuario("Guilherme")
camyla = Usuario("Camyla")
gael = Usuario("Gael")

lance_gui = Lance(gui, 100)
lance_camy = Lance(camyla, 200)
lance_gael = Lance(gael, 20)

leilao = Leilao("Lance de Celulares")
leilao.propoe(lance_gui)
leilao.propoe(lance_gael)
leilao.propoe(lance_camy)

for lance in leilao.lances:
    print(
        f"Usuario: {lance.usuario.nome}\nLance: {lance.valor}\n"
        f"--------------------"
    )
print(
    f"O menor lance foi de: {leilao.menor_lance} \n"
    f"O maior lance foi de: {leilao.maior_lance}"
)
