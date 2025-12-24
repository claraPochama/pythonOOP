from module import User, Accounts

def display_menu():
    print("Option")
    print("1. Show Account detail")
    print("2. Create a new account") # no account at first 
    print("3. Withdraw cash")
    print("4. Deposit funds into your account")
    print("5. Convert funds to another currency")
    print("6. Transfer fund to another account")
    print("7. Switch to another account") 
    print("8. Add new currency")
    print("9. Account History")
    print("10. Exit the online service")
    print()


def main():
    print("Welcome to CUBS online banking service\n")
    bank_accounts = Accounts()
    current_account = ""
    while True:
        if current_account != "":
            print("Current account: " + current_account)
        display_menu()
        try:
            command = int(input("Command: "))
        except ValueError:
            print("Please enter a number.\n")
            continue

        if command == 1:
            # 1. Account detail
            bank_accounts.show_account_detail(current_account)
        
        elif command == 2:
            # 2. Create a new account
            name = str(input("Client name: "))
            email = str(input("Contact email: "))
            country = str(input("Client country: "))
            account_id = str(input("Account ID (not changeable): "))
            bank_accounts.create_user(name, email, country, account_id)
            current_account = account_id
            print("Now switched to " + current_account + "\n")

        elif command == 3:
            # 3. Withdraw cash
            if current_account == "":
                print("No account selected. Please create or switch to an account first.\n")
            else:
                bank_accounts.withdraw_from_account(current_account)

        elif command == 4:
            # 4. Deposit funds into your account
            if current_account == "":
                print("No account selected. Please create or switch to an account first.\n")
            else:
                bank_accounts.deposit_to_account(current_account)

        elif command == 5:
            # 5. Convert funds to another account
            if current_account == "":
                print("No account selected. Please create or switch to an account first.\n")
            else:
                bank_accounts.convert_account_currency(current_account)       
        
        elif command == 6:
            # 6. Transfer funds to another account
            if current_account == "":
                print("No account selected. Please create or switch to an account first.\n")
            else:
                to_account_id = str(input("Enter the account id you would like to transfer fund to: "))
                bank_accounts.transfer_fund(current_account, to_account_id)  

        elif command == 7:
            # 7. Switch to another account
            if len(bank_accounts.account) == 0:
                print("No account to switch. Please create one first.\n")
            else:
                account_id = str(input("Enter the account id you want to switch to: "))
                if bank_accounts.get_account_by_id(account_id) == False:
                    print("Account id not found.\n")
                else:
                    current_account = account_id
                    print("Now switched to " + current_account + "\n")
        elif command == 8:
            # 8. Add new currency
            bank_accounts.add_new_currency_global()

        elif command == 9:
            # 9. Transaction History
            print("Transaction History: \n")
            bank_accounts.transaction_history(current_account)

        elif command == 10:
            # 10. Exit the online service
            break

        else:
            print("Not a valid command. Please try again.\n")
    print("Thank you for using CUBS Online Banking today. Bye!\n")
   
    
if __name__ == "__main__":
    main()
