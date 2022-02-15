arquivo__contatos = open('Estudando/IO/contatos.csv', encoding='UTF-8')
# conteudo = arquivo__contatos.readline()

for line in arquivo__contatos:
    print(line, end="")
