class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): 
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal rejected.")

account = Account("John Doe", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.deposit(300)

# Testing for overdraw (withdrawal exceeding available balance)
account.withdraw(1200)