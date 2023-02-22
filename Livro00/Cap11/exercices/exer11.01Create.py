#Exercice 11.01 - Faça um programa que crie o banco de dados e prices.db com a tabela de preços para armazenar uma lista de preços de venda de produtos. A tabela deve conter o nome do produo e seu respectivo preço. O programa tambpem deve inserir alguns dads para o teste
import sqlite3
connection = sqlite3.connect("prices.db")
cursor = connection.cursor()
cursor.execute('''
    create table PRICEPRODUCTS(
    name text,
    price float)
    ''')
cursor.execute('''
    insert into PRICEPRODUCTS(name, price)
    values(? ,?)
    ''', ("Castanha do Para", 8.90))
connection.commit()
cursor.close()
connection.close()