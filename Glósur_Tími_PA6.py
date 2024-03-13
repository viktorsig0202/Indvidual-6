class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        """Adds accounts to the bank.

        Args:
            account (str): account object to be added to the bank
        """
        self.accounts.append(account)

    def total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    def __str__(self):
        return self.name
