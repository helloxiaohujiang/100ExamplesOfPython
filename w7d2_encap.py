# Implement Encapsulation (Private Variables)

class BankAccount:
    
    acc = "888"
    __accname = "Jack" #private class attribute
    
    def __init__(self,balance):
        self.__balance = balance #private instance vairable

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")  
        return self.__balance
    
    @staticmethod
    def greetings():
        print("Welcome!", BankAccount.__accname)
        
    @classmethod
    def change_acc(cls, newacc):
        cls.acc = newacc
        
    @classmethod
    def get_accname(cls):
        return BankAccount.__accname

b1 = BankAccount(100)

b1.greetings() 
BankAccount.greetings()

print(b1.get_balance())
print(BankAccount.get_balance(b1))  

print(b1.deposit(50))
print(BankAccount.withdraw(b1,50))

print(b1.acc)
print(BankAccount.acc)

b1.change_acc('666')

print(b1.acc)
print(BankAccount.acc)

print(b1.get_accname())
print(BankAccount.get_accname())

print(b1.acc)
print(b1._BankAccount__accname)