class bank:
    def __init__(self, amount):
        self.amount = amount
    def getballance(self):
        print("your ballance is", self.amount)
    def deposit(self, money):
        self.amount += money
        print("you have deposited", money)
    def withdraw(self, money):
        self.amount -= money
        print("you have withdrawn", money)
myaccount = bank(1000)
myaccount.getballance()
myaccount.deposit(500)
myaccount.getballance()
myaccount.withdraw(200)
myaccount.getballance()