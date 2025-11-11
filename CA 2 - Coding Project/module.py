class user:
    def __init__(self, client_name, contact_email, client_region, account_id): 
        self.client_name = client_name
        self.contact_email = contact_email
        self.client_region = client_region
        self.account_id = account_id
    def __str__(self):
        return self.client_name + " (Account ID: " + self.account_id + ")"

class accounts:
    def __init__(self): 
        self.account = []
        #self.account.append(user(user.client_name, user.contact_email, user.client_region, user.account_id, user.list_of_currencies, user.list_of_balance))

    # option 1 
    def show_account_detail(self):
        if len(self.account) != 0:
            for user in self.account:
                print(self.account)
                #print(user(user.client_name, user.contact_email, user.client_region, user.account_id, user.list_of_currencies, user.list_of_balance))
            print()
        else:
            print("No account added yet.")
            print("Please go to Option 5 to create a new account. ")
            print()
    
    #option 5: user data collection
    def create_user(self, name: str, email: str, country: str, account_id: str):
        u = user(name, email, country, account_id)
        self.account.append(u)
        print("New user" + name + account_id + "created.")
        print()
    
    #option 6: switch account