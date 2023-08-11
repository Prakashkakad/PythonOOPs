class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount < 0:
            print("Cannot set a negative balance!")
        else:
            self._balance = amount

    balance = property(get_balance, set_balance)

# Using the BankAccount class
account = BankAccount(1000)

print(account.balance)  # Output: 1000

account.balance = 1500
print(account.balance)  # Output: 1500
account.balance = -500  # Output: Cannot set a negative balance!
