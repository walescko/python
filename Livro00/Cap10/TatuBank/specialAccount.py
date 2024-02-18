from Livro00.Cap10.TatuBank.account import Account


class SpecialAccount(Account):
    def __init__(self, customers, balance = 0, limits = 0):
        Account.__init__(self, customers, number, balance)
        self.limits = limits
    def withdrawal(self, value):
        if self.balance + self.limits >= value:
            self.balance -= value
            self.operators.append(["SAQUE", value])
