import sqlite3

# Conectando e criando tabela
con = sqlite3.connect('meu_BD.db')
cursor = con.cursor()

cursor.execute('''CREATE TABLE "Pessoas" (
            "nome" TEXT,
            "Id" INTERGER
            );''')
con.commit()
