#class and object

class Person:

    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"hello i am {self.name}")

p1 = Person("chandra")
p1.greet()

#Encapsulation
class BankAccount:

    def __init__(self,balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

account = BankAccount(100000)
print(account.get_balance())