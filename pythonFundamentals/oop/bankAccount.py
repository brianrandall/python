class BankAccount:
    accounts = []
    def __init__(self, first_name, last_name, acct_number, int_rate, balance): 
        self.first_name = first_name
        self.last_name = last_name
        self.acct_number = acct_number
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    
    def deposit(self, amount):
        self.balance += amount
        print(f'your deposit of {amount} has been accepted {self.first_name}, and your new balance is {self.balance}')
        return self
    def withdrawl(self, amount):
        if (amount < self.balance):
            self.balance -= amount
            print(f'your withdrawl of {amount} has been accepted {self.first_name}, your new balance is {self.balance}')
        else:
            print('you fool, you have overdrawn your account. $5 fee for you')
            self.balance -= (self.balance - 5)
        return self
    def display_account_info(self):
        print(f'name: {self.first_name} {self.last_name}, account number: {self.acct_number}, balance: {self.balance}')
        return self
    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= (1 + self.int_rate)
            self.balance = "{:.2f}".format(self.balance)
            print(f'your new balance with yeilded interest is {self.balance}')
        else:
            print('nice try...')
    @classmethod
    def print_account_info(cls):
        for accounts in cls.accounts:
            print(f'{accounts.first_name} {accounts.balance}')
            

account1 = BankAccount('brian', 'randall', 54066699, .12, 4000).display_account_info()
account2 = BankAccount('james', 'jamerson', 54066700, .10, 450000).display_account_info()

account1.deposit(20).deposit(4000).deposit(23462).withdrawl(1).yield_interest()
account2.deposit(2345).deposit(10000).withdrawl(3245).withdrawl(44).withdrawl(1.50).withdrawl(62.38).yield_interest()

BankAccount.print_account_info()