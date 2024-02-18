class Bank:
    def __init__(self, name):
        self.name = name
        self.customers =[]
        self.accounts = []
    def open_account(self, account):
        self.accounts.append(account)
    def account_list(self):
        for c in self.accounts:
            c.resume()

