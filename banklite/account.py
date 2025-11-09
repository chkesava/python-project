from datetime import datetime

class Account:
    account_counter = 1

    def __init__(self, name, dob, balance=0.0):
        self.name = name
        self.dob = dob
        self.id = self.generate_account_id()
        self.balance = balance
        self.transactions = []

    def generate_account_id(self):
        bank_prefix = "BL"
        name_initials = ''.join([part[0].upper() for part in self.name.split()])
        dob_formatted = datetime.strptime(self.dob, "%Y-%m-%d").strftime("%Y%m%d")
        account_number = f"{bank_prefix}{name_initials}{dob_formatted}{Account.account_counter:04d}"
        Account.account_counter += 1
        return account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"{datetime.now()} - Deposited ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"{datetime.now()} - Withdrew ₹{amount:.2f}")

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.transactions

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dob": self.dob,
            "balance": self.balance,
            "transactions": self.transactions
        }

    @staticmethod
    def from_dict(data):
        account = Account.__new__(Account)
        account.name = data['name']
        account.dob = data['dob']
        account.id = data['id']
        account.balance = data['balance']
        account.transactions = data['transactions']
        return account
