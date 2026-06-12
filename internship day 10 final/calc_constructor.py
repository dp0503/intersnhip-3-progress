class bank:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def add(self):
        print("the sum is", self.a + self.b)
    def delete(self, a , b):
        print("the difference is", self.a - self.b)
    def mul(self, money):
        print("the product is", self.a * self.b)
myaccount = bank(1000, 500)
myaccount.add()
myaccount.delete(1000, 500)
myaccount.mul(1000)