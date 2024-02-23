#Programa 11.1 - Consulta com múltiplos resultados sem cursores
import sqlite3
with sqlite3.connect("diaryTelephone.db") as connection:
    for register in connection.execute("select * from diaryTelephone"):
        print(f"Nome: {register[0]}\nTelefone: {register[1]}")
