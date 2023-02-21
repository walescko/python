#Programa 11.4 - Consulta com filtro de seleção
import sqlite3
from contextlib import closing

name = input("Nome a procurar: ")
with sqlite3.connect("diaryTelephone.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM DIARYTELEPHONE WHERE NAME = '{name}'")
        while True:
            result = cursor.fetchone()
            if result is None:
                break
            print(f"Nome: {result[0]}\nTelefone: {result[1]}")
