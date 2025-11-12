class User:
    def __init__(self, 
                    client_name, 
                    contact_email, 
                    client_region, 
                    account_id, 
                    account_currency, 
                    account_balance): 
        
        self.client_name = client_name
        self.contact_email = contact_email
        self.client_region = client_region
        self.account_id = account_id
        self.account_currency = account_currency
        self.account_balance = account_balance
        
    def __str__(self):
        return (
            "Account ID: " + self.account_id + 
            "/n Name: " + self.client_name + 
            "/n Email: " + self.contact_email + 
            "/n Region: " + self.client_region)

class Accounts:
    def __init__(self): 
        self.account = []
        

    # option 1 + edit detail function
    def show_account_detail(self):

        if len(self.account) != 0:

            for user in self.account:
                print(user)
                #print(user(user.client_name, user.contact_email, user.client_region, user.account_id, user.list_of_currencies, user.list_of_balance))
            
            print()
            edit_option = str(
                input(
            "Press E to edit Account detail or any key to go back to Main Menu. "))
            
            if edit_option.lower() == "e":
                self.edit_account_detail(
                    str(input("Enter the account id you want to edit details:")))
            else: return
        else:
            
            print("No account added yet.")
            print("Please go to Option 5 to create a new account. ")
            print()

    def edit_account_detail(self, 
                            account_to_be_edited):
        #find the account to be edited
        for user in self.account:
            if user.account_id == account_to_be_edited:
                account_to_be_edited = user
                break

        edit_detail = str(
            input("Enter name/email/region to change: "))
        if edit_detail.lower() == "name":
            new_detail = str(
                input("Enter a new name:"))
            account_to_be_edited.client_name = new_detail

        elif edit_detail.lower() == "email":
            new_detail = str(
                input("Enter a new email:"))
            account_to_be_edited.contact_email = new_detail

        elif edit_detail.lower() == "region":
            new_detail = str(
                input("Enter another region:"))
            account_to_be_edited.client_region = new_detail
            
        else:
            print("Not a valid input. Returning to main menu.\n")
            return
        
        print("Account detail updated.\n")

    #option 5: user data collection
    def create_user(self, 
                    name, 
                    email, 
                    country, 
                    account_id, 
                    account_currency): 
        
        if (account_currency.lower() != "EUR" and 
            account_currency.lower() != "GBP" and 
            account_currency.lower() != "USD"):

            print("Not a valid input. Please try again.\n")
            
        user = User(name, 
                 email, 
                 country, 
                 account_id, 
                 account_currency)
        
        self.account.append(user)

        print(
            "New user" + 
            name + 
            account_id + "created.")
        
        print()
    
    
    #option 6: switch account