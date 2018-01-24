
class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def has_id(self,target_id):
        if target_id == self.id:
            return True

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('No action: Amount greater than available balance.')
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def get_balance(self):
        return self.balance


