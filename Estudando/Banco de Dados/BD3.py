import sqlite3

con = sqlite3.connect("meu_BD.db")
cursor = con.cursor()

x = cursor.execute("SELECT * from Pessoas")
for i in x:
    print(i)
