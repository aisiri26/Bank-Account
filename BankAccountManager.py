from BankAccount import BankAccount

class BankAccountManager:
    def __init__(self):
        self.account_list = []

    def add_account(self, customer_id, name, init_balance):
        self.account_list.append(BankAccount(customer_id, name, init_balance))


    def checkID(self, customer_id):
       i = 0
       while i != len(self.account_list):
           if self.account_list[i].has_id(customer_id) == True:
               return i
           else:
               i = i + 1
       raise RuntimeError('No account found!')

    def make_deposit(self, customer_id, amount):
        index = self.checkID(customer_id)
        self.account_list[index].deposit(amount)


    def make_withdrawl(self, customer_id, amount):
        index = self.checkID(customer_id)
#        print index
        self.account_list[index].withdraw(amount)

    def get_balance(self, customer_id):
        index = self.checkID(customer_id)
        self.account_list[index].get_balance()

    def get_account_report(self, customer_id):
        index = self.checkID(customer_id)
        data = (customer_id, self.account_list[index].name, self.account_list[index].get_balance())
        format_string = ("ID: %s\n"
                             "Name: %s\n"
                             "Balance: %.02f\n")
        return format_string % data


