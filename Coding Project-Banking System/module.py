class User:
    # class for one bank user
    def __init__(self, 
            client_name, 
            contact_email, 
            client_region, 
            account_id
            ): 

        self.client_name = client_name
        self.contact_email = contact_email
        self.client_region = client_region
        self.account_id = account_id

        # default currencies (same index as balances)
        self.list_of_currencies = ["EUR", "USD", "GBP"]
        self.list_of_balances = [0.0, 0.0, 0.0]
        self.list_of_history = []

    def __str__(self):
        # show basic user info
        return (
            "Account ID: " + self.account_id 
            + "\nName: " + self.client_name 
            + "\nEmail: " + self.contact_email 
            + "\nRegion: " + self.client_region
            + "\n")

    def show_balances(self):
        # print all balances
        print("Balances:")
        for i in range(len(self.list_of_currencies)):
            print(self.list_of_currencies[i] + ": " + str(self.list_of_balances[i]))
        print()

    # put money in one currency
    def deposit(self, currency_index, amount):
        if amount <= 0:
            return False
        self.list_of_balances[currency_index] = self.list_of_balances[currency_index] + amount
        return True

    # take money from one currency
    def withdraw(self, currency_index, amount):
        if amount <= 0:
            return False
        if amount > self.list_of_balances[currency_index]:
            return False
        self.list_of_balances[currency_index] = self.list_of_balances[currency_index] - amount
        return True

    # convert money between 2 currencies for same user
    def convert(self, from_index, to_index, amount, rate, fee_percent):
        if amount <= 0:
            return False, 0.0
        if amount > self.list_of_balances[from_index]:
            return False, 0.0

        # remove from source
        self.list_of_balances[from_index] = self.list_of_balances[from_index] - amount

        # do conversion
        converted = amount * rate
        fee = round(converted * fee_percent, 2)
        converted = converted - fee

        # add to target
        self.list_of_balances[to_index] = self.list_of_balances[to_index] + converted

        return True, fee

    # add one new currency to this user
    def add_currency(self, currency_code):
        # only add if not already there
        if currency_code not in self.list_of_currencies:
            self.list_of_currencies.append(currency_code)
            self.list_of_balances.append(0.0)

    def records(self, action: str, result: str):
        history = action + result + str("\n")
        self.list_of_history.append(history)

# --------------------------------------------------------------------------

class Accounts:
    # class to store many users
    def __init__(self): 

        self.account = []

        # Table 1: sample conversion rate to EURO
        # this means: 1 currency unit = rate_to_euro[currency] euros
        self.rate_to_euro = {
            "EUR": 1.0,   # EURO
            "USD": 1.1,   # DOLLAR
            "GBP": 0.9    # POUND 
        }

    

    # find user by account id
    def get_account_by_id(self, account_id):
        for user in self.account:
            if user.account_id == account_id:
                return user
        return False
    
    #define fee amount per transaction
    def conversion_fee_percent(self, transaction_amount):
        if transaction_amount < 100:
            fee = 0.01
        elif transaction_amount >= 100 and transaction_amount <= 200: 
            fee = 0.02
        else:
            fee = 0.03
        return fee 

    # option 1: show all users and balances
    def show_account_detail(self, account_id):
        if len(self.account) != 0:
            user = self.get_account_by_id(account_id)
            if user == False:
                print("Account not found.\n")
                return
            print("--Current Account Info--")
            print(user)
            user.show_balances()
            print()
            edit_option = str(
                input("Press E to edit Account detail (Current account: " + account_id 
                      +") or any key to go back to Main Menu. ")
                    )
            
            if edit_option.lower() == "e":
                self.edit_account_detail(account_id)
            else: 
                return
        else:
            print("No account added yet.")
            print("Please go to Option 2 to create a new account. ")
            print()

    # edit simple user fields
    def edit_account_detail(self, account_to_be_edited):
        # find the account to be edited
        found_account = False
        for user in self.account:
            if user.account_id == account_to_be_edited:
                found_account = user
                break

        if found_account == False:
            print("Account id not found.\n")
            return
                  
        account_to_be_edited = found_account

        edit_detail = str(
            input("Enter name/email/region to change: ")
            )

        if edit_detail.lower() == "name":
            new_detail = str(
                input("Enter a new name: ")
                )
            account_to_be_edited.client_name = new_detail

        elif edit_detail.lower() == "email":
            new_detail = str(
                input("Enter a new email: ")
                )
            account_to_be_edited.contact_email = new_detail

        elif edit_detail.lower() == "region":
            new_detail = str(
                input("Enter another region: ")
                )
            account_to_be_edited.client_region = new_detail

        else:
            print("Not a valid input. Returning to main menu.\n")
            return
        print("Account detail updated.\n")
        user.records(edit_detail.lower() + " update", new_detail)

    # option 2: create new user and set starting balances
    def create_user(self, 
            name: str, 
            email: str, 
            country: str,
            account_id: str
            ):

        new_user = User(
                name, 
                email, 
                country, 
                account_id
                )

        # set starting balances
        print("Set starting balances (0 means no money).")
        for i in range(len(new_user.list_of_currencies)):
            currency = new_user.list_of_currencies[i]
            try:
                amount = float(input("Initial balance for " + currency + ": "))
            except ValueError:
                print("Invalid input. The initial amount is set as 0.0.")
                amount = 0.0
            new_user.list_of_balances[i] = amount

        self.account.append(new_user)

        print(
            "New user " 
            + name + " (" + account_id + ") "
            + "created."
              )
        new_user.records("New user " + name + " (" + account_id + ") ", "created.")
        print()
    
    # option 3: withdraw cash
    def withdraw_from_account(self, account_id):
        user = self.get_account_by_id(account_id)
        if user == False:
            print("Account not found.\n")
            return

        user.show_balances()
        currency_code = str(input("Enter currency code to withdraw from (ex. EUR): "))
        currency_code = currency_code.upper()

        if currency_code not in user.list_of_currencies:
            print("Currency not in this account.\n")
            return

        index = user.list_of_currencies.index(currency_code)

        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Not a number.\n")
            return

        ok = user.withdraw(index, amount)
        if ok:
            print("Withdraw done.")
            user.records("Cash withdraw", str(amount) + " " + str(currency_code))
            user.show_balances()
        else:
            print("Not enough balance or wrong amount.\n")

    # option 4: deposit funds
    def deposit_to_account(self, account_id):
        user = self.get_account_by_id(account_id)
        if user == False:
            print("Account not found.\n")
            return

        user.show_balances()
        currency_code = str(input("Enter currency code to deposit to (ex. EUR): "))
        currency_code = currency_code.upper()

        if currency_code not in user.list_of_currencies:
            print("Currency not in this account.\n")
            return

        index = user.list_of_currencies.index(currency_code)

        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Not a number.\n")
            return

        ok = user.deposit(index, amount)
        if ok:
            print("Deposit done.")
            user.records("Cash deposit", str(amount) + " " + str(currency_code))
            user.show_balances()
        else:
            print("Wrong amount.\n")

    # option 5: convert between currencies in same account
    def convert_account_currency(self, account_id):
        user = self.get_account_by_id(account_id)
        if user == False:
            print("Account not found.\n")
            return

        user.show_balances()

        from_currency = str(input("Convert FROM currency (ex. EUR): "))
        to_currency = str(input("Convert TO currency (ex. USD): "))

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in user.list_of_currencies:
            print("From currency not in this account.\n")
            return

        if to_currency not in user.list_of_currencies:
            print("To currency not in this account.\n")
            return

        '''if from_currency == to_currency:
            print("Currencies are the same.\n")
            return '''

        # check we have rate to euro for both
        if from_currency not in self.rate_to_euro or to_currency not in self.rate_to_euro:
            print("No rate for this conversion.\n")
            return

        try:
            amount = float(input("Amount to convert (from " + from_currency + "): "))
        except ValueError:
            print("Not a number.\n")
            return
        
        if amount <= 0:
            print("Please input a valid amount. \n")
            return

        from_index = user.list_of_currencies.index(from_currency)
        to_index = user.list_of_currencies.index(to_currency)

        
        # factor from A to B = rate_to_euro[A] / rate_to_euro[B]
        rate = self.rate_to_euro[from_currency] / self.rate_to_euro[to_currency]
        fee_percent = self.conversion_fee_percent(amount)

        transaction_status, fee = user.convert(
            from_index, to_index, 
            amount, rate, 
            fee_percent)

        if transaction_status:
            print("Conversion done.")
            user.records("Conversion" + str(amount) + str(to_currency), " to " + str(to_index))
            print("Fee charged: " + str(fee))
            user.show_balances()
        else:
            print("Not enough balance or unexpected error.\n")


    def transfer_fund(self, from_account_id, to_account_id):
        to_user = self.get_account_by_id(to_account_id)
        if to_user == False:
            print("Account not found.\n")
            return
        from_user = self.get_account_by_id(from_account_id)
        if to_user == from_user:
            print("You cannot transfer fund to yourself. Please go to option 5 for converting different currencies.\n")
            return
        print(str(from_account_id) + ":")
        from_user.show_balances()

        from_currency = str(input("Convert FROM currency (ex. EUR): "))
        to_currency = str(input("Convert TO currency (ex. USD): "))

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in from_user.list_of_currencies:
            print("From currency not in this account.\n")
            return

        if to_currency not in to_user.list_of_currencies:
            print("To currency not in this account.\n")
            return

        # check we have rate to euro for both
        if from_currency not in self.rate_to_euro or to_currency not in self.rate_to_euro:
            print("No rate for this conversion.\n")
            return

        try:
            amount = float(input("Amount to convert (from " + from_currency + "): "))
        except ValueError:
            print("Not a number.\n")
            return
        
        if amount <= 0:
            print("Please input a valid amount. \n")
            return

        from_index = from_user.list_of_currencies.index(from_currency)
        if from_user.list_of_balances[from_index] < amount:
            print("Sender has insufficient funds.\n")
            return
        
        to_index = to_user.list_of_currencies.index(to_currency)

        
        # factor from A to B = rate_to_euro[A] / rate_to_euro[B]
        rate = self.rate_to_euro[from_currency] / self.rate_to_euro[to_currency]
        fee_percent = self.conversion_fee_percent(amount)
        converted = amount * rate
        fee = round(converted * fee_percent, 2)
        converted = converted - fee

        from_user.list_of_balances[from_index] -= amount
        to_user.list_of_balances[to_index] += converted
        print("Successfully transfered fund to: " + str(to_user.account_id),
            ", amount: " + str(amount) + str(from_currency) 
            + ", (fee:" + str(fee) + str(to_currency) + ".)")

        from_user.records("Transfered fund to: " + str(to_user.account_id),
            ", amount: " + str(amount) + str(from_currency) 
            + ", (fee:" + str(fee) + str(to_currency) + ".)")
        to_user.records("Received fund from: " + str(from_user.account_id),
            ", amount: " + str(converted) + str(to_currency))


    # add new currency to whole system
    def add_new_currency_global(self):
        # ask user for new code and rate to euro
        code = str(input("New currency code (ex. JPY): "))
        code = code.upper()

        if code in self.rate_to_euro:
            print("Currency already exists.\n")
            return

        try:
            rate = float(input("Conversion rate to EURO (1 unit = ? EUR): "))
        except ValueError:
            print("Not a number.\n")
            return

        if rate <= 0:
            print("Rate must be positive.\n")
            return

        # store rate
        self.rate_to_euro[code] = rate

        # add new currency to all user accounts
        for user in self.account:
            user.add_currency(code)

        print("New currency " + code + " added with rate " + str(rate) + " to EURO.\n")
    
    # check action history
    def transaction_history(self, account_id):
        user = self.get_account_by_id(account_id)
        if user == False:
            print("Account not found.\n")
            return
                      
        print(user.list_of_history)
        
