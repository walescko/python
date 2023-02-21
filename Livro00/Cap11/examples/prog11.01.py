#Programa 11.1 - Consulta com múltiplos resultados
import sqlite3
connection = sqlite3.connect("diaryTelephone.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM DIARYTELEPHONE")
result = cursor.fetchall()
for register in result:
    print(f"Nome: {register[0]}\nTelefone: {register[1]}")
cursor.close()
connection.close()
