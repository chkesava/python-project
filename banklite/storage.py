import json
from banklite.account import Account

def save_to_file(accounts, filename):
    with open(filename, "w") as f:
        json.dump([acc.to_dict() for acc in accounts], f, indent=4)

def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            accounts = [Account.from_dict(acc) for acc in data]
            Account.account_counter = len(accounts) + 1
            return accounts
    except FileNotFoundError:
        return []