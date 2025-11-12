from module import User, Accounts

def display_menu():
    print("Option")
    print("1. All Account detail")
    print("2. Withdraw cash")
    print("3. Deposit funds into your account")
    print("4. Convert funds to another account")
    print("5. Create a new account") # no account at first 
    print("6. Switch to another account") # need [[]]
    print("7. Exit the online service")
    print()


def main():
    print("Welcome to CUBS online banking service\n")
    #client = user(name, email, country, account_id)
    bank_accounts = Accounts()
    current_account = ""
    while True:
        display_menu()
        command = int(input("Command: "))
        if command == 1:
            bank_accounts.show_account_detail()

        elif command == 2:
            command_grab(inventory)

        elif command == 3:
            command_edit(inventory)

        elif command == 4:
            command_drop(inventory)

        elif command == 5:
            name = str(input("New Client name: "))
            email = str(input("Contact email: "))
            country = str(input("Client country: "))
            account_id = str(input("New Account ID (not changeable): "))
            account_currency = str(input("Choose 1 currency (EUR/USD/BGP): "))
            bank_accounts.create_user(name, email, country, account_id, account_currency)
            current_account = account_id
            print("Now switch to " + current_account "./n")

        elif command == 6:
            command_drop(inventory)

        elif command == 7:
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
   
    
if __name__ == "__main__":
    main()