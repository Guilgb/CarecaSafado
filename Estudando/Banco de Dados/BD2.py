import sqlite3

con = sqlite3.connect('meu_BD.db')
cursor = con.cursor()

nome = str(input("Digite seu nome: "))
idade = input("Digite sua idade: ")

cursor.execute(f"INSERT INTO Pessoas VALUES ('{nome}', {idade})")
con.commit()
