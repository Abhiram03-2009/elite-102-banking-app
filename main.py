import db

def print_menu():
    print("\n--- Python Banking System ---")
    print("1. Create new bank account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check account balance")
    print("5. List all accounts")
    print("6. Exit")
    print("-----------------------------")

def main():
    db.init_db()
    print("Database initialized.")
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter account holder name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                initial_deposit = float(input("Enter initial deposit amount: "))
                if initial_deposit < 0:
                    print("Initial deposit cannot be negative.")
                    continue
                acc_id = db.create_account(name, initial_deposit)
                print(f"Account created successfully! Account ID: {acc_id}")
            except ValueError:
                print("Invalid amount entered. Please enter a number.")
                
        elif choice == '2':
            try:
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter amount to deposit: "))
                db.deposit(acc_id, amount)
                print("Deposit successful.")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            try:
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter amount to withdraw: "))
                db.withdraw(acc_id, amount)
                print("Withdrawal successful.")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '4':
            try:
                acc_id = int(input("Enter account ID: "))
                balance = db.check_balance(acc_id)
                print(f"Current Balance for Account {acc_id}: ${balance:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '5':
            accounts = db.list_accounts()
            if not accounts:
                print("No accounts found.")
            else:
                print("\nID | Name | Balance")
                print("-------------------")
                for acc in accounts:
                    print(f"{acc[0]} | {acc[1]} | ${acc[2]:.2f}")
                    
        elif choice == '6':
            print("Thank you for using the Banking System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
