import sqlite3
data = [("Castanha de Caju", 12.90),
         ("Aveia Fina", 1.29),
         ("Tâmara", 4.90)]
connection = sqlite3.connect("prices.db")
cursor = connection.cursor()
cursor.executemany('''
    insert into PRICEPRODUCTS(name,price)
    values(?, ?)
    ''', data)
connection.commit()
cursor.close()
connection.close()
