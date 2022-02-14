arquivo__contatos = open('Estudando/IO/contatos.csv', encoding='UTF-8')
conteudo = arquivo__contatos.readlines()


for linha in conteudo:
    print(linha, end="")
