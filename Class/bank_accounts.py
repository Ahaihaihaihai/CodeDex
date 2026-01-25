class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = int(account_id)
        self.account_type = account_type
        self.pin = int(pin)
        self.balance = float(balance)

    def deposit(self, money):
        self.balance += money
        return self.balance
    
    def withdraw(self, money):
        self.balance -= money
        return self.balance
    
    def display_balance(self):
        print(self.balance)

my = BankAccount("Arif Gunadi", "Satriadi", 1234, "Debit", 123456, 10000)
print(f'Your balance after deposit: ${my.deposit(96)}')
print(f'Your balance after withdraw: ${my.withdraw(25)}')
my.display_balance()
