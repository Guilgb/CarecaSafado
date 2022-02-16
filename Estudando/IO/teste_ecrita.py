arquivo_de_contatos = open(
    'Estudando/IO/contatos_escrita.csv', encoding="UTF-8", mode="a+"
)

contatos = [
    '11, Carol, carol@carol.com.br\n',
    '12, Ana, ana@ana.com.br\n',
    '13 Tais, tais@tais.com.br\n',
    '14 Felipe, felipe@felipe.com.br\n'
]

for contato in contatos:
    arquivo_de_contatos.write(contato)

arquivo_de_contatos.flush()

arquivo_de_contatos.seek(0)
for line in arquivo_de_contatos:
    print(line)

input("Pressione <Enter> para encerrar o programa")
