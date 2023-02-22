import sqlite3
connection = sqlite3.connect("prices.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM PRICEPRODUCTS")
while True:
    result = cursor.fetchone()
    if result is None:
        break
    print(f"Produto: {result[0]}\nPreço: R${result[1]:.2f}\n")
cursor.close()
connection.close()