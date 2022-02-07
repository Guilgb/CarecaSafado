import re
# padrão é um numero uma letra e outro numero
padrao = "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
texto = "123 1a2 1cc aa1 99135590"
resposta = re.search(padrao, texto)
print(resposta.group())

padrao_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto_email = "asdba a asuhdiua  haiushd aiusdhia o guilhermegb@hotmail.com.br"
resposta_email = re.search(padrao_email, texto_email)
print(resposta_email.group())
