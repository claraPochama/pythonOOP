class user:
    def __init__(self, client_name, contact_email, client_region, account_id, list_of_currencies, list_of_balance): 
        self.client_name = client_name
        self.contact_email = contact_email
        self.client_region = client_region
        self.account_id = account_id
        self.list_of_currencies = list_of_currencies
        self.list_of_balance = list_of_balance
    def __str__(self):
        return self.client_name + " (Account ID: " + self.account_id + ")"

class accounts:
    def __init__(self): 
        self.account = []
        self.account.append(user(user.client_name, user.contact_email, user.client_region, user.account_id, user.list_of_currencies, user.list_of_balance))
    def show_account_detail(self):
        for users in self.account:
            print(user(user.client_name, user.contact_email, user.client_region, user.account_id, user.list_of_currencies, user.list_of_balance))
        print()
    def 

