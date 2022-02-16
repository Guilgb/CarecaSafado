arquivo_de_contatos = open(
    'Estudando/IO/contatos_escrita.csv', encoding="UTF-8", mode="a")

contato = '11, Carol, carol@carol.com.br\n'
arquivo_de_contatos.write(contato)
