from customers import Customers
from account import Account

jonh = Customers("Jonh Gaspar", "234-5678")
mary = Customers("Mary", "876-5432")

account1 = Account(["Jonh Gaspar", 1, 1000])
account2 = Account(["Mary Gaspar", 2, 500]) #é possível de fazer o number ser incrementando automaticamente com uma função
account1.withdrawal(50)
account2.deposit(300)
account1.withdrawal(190)
account2.deposit(95.15)
account2.withdrawal(250)
account1.statement()
account2.statement()


