from banklite.bank import Bank
from banklite.utils import is_valid_amount

def main():
    bank = Bank()
    bank.load_from_file("bank.json")

    while True:
        print("\n--- BankLite Console ---")
        print("1. Create Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. View Balance")
        print("5. View Transaction History")
        print("6. Save Data")
        print("7. Exit")
        print("8. Transfer Funds")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            balance_input = input("Enter initial balance: ")
            if not is_valid_amount(balance_input):
                print("Invalid amount.")
                continue
            balance = float(balance_input)
            try:
                acc_id = bank.create_account(name, dob, balance)
                print(f"Account created successfully. ID: {acc_id}")
            except Exception as e:
                print(f"Error creating account: {e}")

        elif choice == "2":
            acc_id = input("Enter account ID: ")
            amount_input = input("Enter amount to deposit: ")
            if not is_valid_amount(amount_input):
                print("Invalid amount.")
                continue
            amount = float(amount_input)
            try:
                if bank.deposit_to_account(acc_id, amount):
                    print("Deposit successful.")
                else:
                    print("Account not found.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            acc_id = input("Enter account ID: ")
            amount_input = input("Enter amount to withdraw: ")
            if not is_valid_amount(amount_input):
                print("Invalid amount.")
                continue
            amount = float(amount_input)
            try:
                if bank.withdraw_from_account(acc_id, amount):
                    print("Withdrawal successful.")
                else:
                    print("Account not found.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            acc_id = input("Enter account ID: ")
            acc = bank.find_account_by_id(acc_id)
            if acc:
                print(f"Current Balance: ₹{acc.get_balance():.2f}")
            else:
                print("Account not found.")

        elif choice == "5":
            acc_id = input("Enter account ID: ")
            details = bank.show_account_details(acc_id)
            if details:
                print(f"Name: {details['name']}")
                print(f"DOB: {details['dob']}")
                print(f"Balance: ₹{details['balance']:.2f}")
                print("Transaction History:")
                for txn in details['transactions']:
                    print(txn)
            else:
                print("Account not found.")

        elif choice == "6":
            bank.save_to_file("bank.json")
            print("Data saved successfully.")

        elif choice == "7":
            bank.save_to_file("bank.json")
            print("Exiting... Goodbye!")
            break
        elif choice == "8":
            from_id = input("Enter sender's account ID: ")
            to_id = input("Enter receiver's account ID: ")
            amount_input = input("Enter amount to transfer: ")
            if not is_valid_amount(amount_input):
                print("Invalid amount.")
                continue
            amount = float(amount_input)
            try:
                bank.transfer_funds(from_id, to_id, amount)
                print(f"₹{amount:.2f} transferred from {from_id} to {to_id}.")
            except ValueError as e:
                print(f"Transfer failed: {e}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
