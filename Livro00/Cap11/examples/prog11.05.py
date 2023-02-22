#Programa 11.5 - Consulta utlizando parâmetros
import sqlite3
from contextlib import closing

name = input("Nome a selecionar: ")
with sqlite3.connect("diaryTelephone.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('SELECT * FROM DIARYTELEPHONE WHERE NAME = ?', (name,))
        x = 0
        while True:
            result = cursor.fetchone()
            if result is None:
                if x == 0:
                    print('Nada encontrado.')
                break
            print(f"Nome: {result[0]}\nTelefone: {result[1]}")
            x += 1
