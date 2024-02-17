class Account:
    def __init__(self, customers, number, balance=0):
        self.balance = 0
        self.customers = customers
        self.number = number
        self.operators = []
        self.deposit(balance)
    def resume(self):
        print(f"CC Número: {self.number} Saldo: {self.balance:10.2f}")
    def withdrawal(self, value):
        if self.balance >= value:
            self.saldo -= value
            self.operators.append(["SAQUE", value])
    def deposit(self, value):
        self.balance += value
        self.operators.append(["DEPOSITO", value])
    def statement(self):
        print(f"Extrato CC Nº {self.number}\n")
        for o in self.operators:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n   Saldo: {self.balance:10.2f}\n")