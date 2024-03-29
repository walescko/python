#Programa 11.4 - Consulta com filtro de seleção
import sqlite3
from contextlib import closing
with sqlite3.connect("diaryTelephone.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM DIARYTELEPHONE WHERE NAME = 'Japir Adão'")
        while True:
            result = cursor.fetchone()
            if result is None:
                break
            print(f"Nome: {result[0]}\nTelefone: {result[1]}")
