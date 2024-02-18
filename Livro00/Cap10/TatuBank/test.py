from customers import Customers
from account import Account
from bank import Bank

jonh = Customers("Jonh Gaspar", "234-5678")
mary = Customers("Mary", "876-5432")
joseph = Customers("Joseph", "321-9873")

accountJM = Account([jonh, mary], 100)
contaJ = Account([joseph], 10)
tatu = Bank("Tatú")
tatu.open_account(accountJM)
tatu.open_account(contaJ)
tatu.account_list()

# account1 = Account(["Jonh Gaspar", 1, 1000])
# account2 = Account(["Mary Gaspar", 2, 500]) #é possível de fazer o number ser incrementando automaticamente com uma função
# account1.withdrawal(50)
# account2.deposit(300)
# account1.withdrawal(190)
# account2.deposit(95.15)
# account2.withdrawal(250)
# account1.statement()
# account2.statement()


