import sqlite3
from contextlib import closing

data = ['pegar da internet']

with sqlite3.connect("brasil.db") as connection:
    connection.row_factory = sqlite3.Row
    with closing(connection.cursor()) as cursor:
        cursor.execute("""CREATE TABLE estados(id integer primary key autoincrement,
                        name text,
                        population integer)
                    """),
        cursor.executemany("INSERT INTO estados(name, population) values(?,?)", data)
    connection.commit()
    