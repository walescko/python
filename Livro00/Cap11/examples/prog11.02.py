#Programa 11.2 - Consulta, registro por registro
import sqlite3
connection = sqlite3.connect("diaryTelephone.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM DIARYTELEPHONE")
while True:
    result = cursor.fetchone()
    if result is None:
        break
    print(f"Nome: {result[0]}\nTelefone: {result[1]}\n")
cursor.close()
connection.close()
