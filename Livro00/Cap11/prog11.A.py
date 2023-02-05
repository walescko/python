#test agenda.db - fundaments
import sqlite3
connection = sqlite3.connect("diaryTelephone.db")
cursor = connection.cursor()
cursor.execute('''
    create table diaryTelehpne(
    name text,
    telephone text)
    ''')
cursor.execute('''
    insert into diaryTelephone (name, telephone)
    values(? ,?)
    ''', ("Pensador", "2345-6789"))
connection.commit()
cursor.close()
connection.close()
