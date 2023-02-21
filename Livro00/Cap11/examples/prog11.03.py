#Programa 11.3 - Uso do with para fechar a conexão
import sqlite3
from contextlib import closing
with sqlite3.connect("diaryTelephone.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM DIARYTELEPHONE")
        while True:
            result = cursor.fetchone()
            if result is None:
                break
            print(f"Nome: {result[0]}\nTelefone: {result[1]}\n")
