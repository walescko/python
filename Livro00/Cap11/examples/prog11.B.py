#read database
import sqlite3
connection = sqlite3.connect("diaryTelephone.db")
cursor = connection.cursor()
cursor.execute("select * from diaryTelephone")
result = cursor.fetchone()
print(f"Nome: {result[0]}\nTelefone: {result[1]}")
cursor.close()
connection.close()
