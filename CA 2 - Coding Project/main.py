from module import user, accounts

def display_menu():
    print("Option")
    print("1. Account detail")
    print("2. Withdraw cash")
    print("3. Deposit funds into your account")
    print("4. Convert funds to another account")
    print("5. Create a new account") # no account at first 
    print("6. Switch to another account") # need [[]]
    print("7. Exit the online service")
    print()


def main():
    print("Welcome to CUBS online banking service\n")
    display_menu()
    while True:
        command = int(input("Command: "))
        if command.lower() == 1:
            command_show(inventory)
        elif command.lower() == 2:
            command_grab(inventory)
        elif command.lower() == 3:
            command_edit(inventory)
        elif command.lower() == 4:
            command_drop(inventory)
        elif command.lower() == 5:
            command_drop(inventory)
        elif command.lower() == 6:
            command_drop(inventory)
        elif command.lower() == 7:
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
   
    
if __name__ == "__main__":
    main()