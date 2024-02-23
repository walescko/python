#Programa 11.6 - Exemplo de update sem where e com rowcount
import sqlite3
from contextlib import closing

with sqlite3.connect("diaryTelephone.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("""updade agenda
                        set telephone = '2344-1234'
                    """)
        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            connection.commit()
            print("Alterações realizada com sucesso!")
        else:
            connection.rollback()
            print("Alteções não foram realizadas")

