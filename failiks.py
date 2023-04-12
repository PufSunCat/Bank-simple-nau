import datetime

class Customer:
    def __init__(self, name, surname, id, email):
        self.name = name
        self.surname = surname
        self.id = id
        self.email = email
        self.datetime_created = datetime.datetime.now()
        self.accounts = []

    def status(self):
        print(f"Client: {self.name} {self.surname} ({self.id}) {self.datetime_created}")

    def add_account(self, number, currency, balance):
        self.accounts.append(Account(number, currency, balance))
    
    def print_accounts(self):
        for account in self.accounts:
            account.status()


class Account:
    def __init__(self, number, currency, balance, status = 'Active'):
        self.number = number
        self.currency = currency
        self.balance = balance
        self.account_status = status
        self.datetime_created = datetime.datetime.now()

    def status(self):
        print(f"Account: {self.number} ({self.currency}) {self.balance} {self.account_status}")
        

customer1 = Customer("Anna", "Bērziņa", "78987-65448", "annab@someemail.co")
customer1.add_account("123456789", "EUR", 200)
customer1.add_account("987654321", "USD", 100)

customer1.status()
customer1.print_accounts()
