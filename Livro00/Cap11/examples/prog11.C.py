#insert new data in database
import sqlite3
data = [("Oscar Eca", "98901-0109"),
         ("Misca Bella", "98902-8900"),
         ("Japir Adão", "97891-3321")]
connection = sqlite3.connect("diaryTelephone.db")
cursor = connection.cursor()
cursor.executemany('''
    insert into diaryTelephone(name,telephone)
    values(?, ?)
    ''', data)
connection.commit()
cursor.close()
connection.close()
