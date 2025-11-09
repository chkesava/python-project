from banklite.account import Account
from banklite.storage import save_to_file, load_from_file
from datetime import datetime

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, dob, initial_balance=0.0):
        account = Account(name, dob, initial_balance)
        self.accounts.append(account)
        return account.id

    def find_account_by_id(self, account_id):
        for acc in self.accounts:
            if acc.id == account_id:
                return acc
        return None

    def deposit_to_account(self, account_id, amount):
        acc = self.find_account_by_id(account_id)
        if acc:
            acc.deposit(amount)
            return True
        return False

    def withdraw_from_account(self, account_id, amount):
        acc = self.find_account_by_id(account_id)
        if acc:
            acc.withdraw(amount)
            return True
        return False

    def show_account_details(self, account_id):
        acc = self.find_account_by_id(account_id)
        if acc:
            return {
                "name": acc.name,
                "dob": acc.dob,
                "balance": acc.get_balance(),
                "transactions": acc.get_history()
            }
        return None

    def save_to_file(self, filename="bank.json"):
        save_to_file(self.accounts, filename)

    def load_from_file(self, filename="bank.json"):
        self.accounts = load_from_file(filename)
    
    def transfer_funds(self, from_account_id, to_account_id, amount):
        from_acc = self.find_account_by_id(from_account_id)
        to_acc = self.find_account_by_id(to_account_id)

        if not from_acc or not to_acc:
            raise ValueError("One or both account IDs are invalid.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if from_acc.balance < amount:
            raise ValueError("Insufficient funds in source account.")

        from_acc.withdraw(amount)
        to_acc.deposit(amount)

        from_acc.transactions.append(f"{datetime.now()} - Transferred ₹{amount:.2f} to {to_acc.id}")
        to_acc.transactions.append(f"{datetime.now()} - Received ₹{amount:.2f} from {from_acc.id}")
        return True
