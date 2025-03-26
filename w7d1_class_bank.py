# Create a Class for a Bank Account

class Bank:
    
    bank_name = "Trust Bank" # class attribute
    
    def __init__(self, name):
        self.name = name # instantce attribute

    def branch(self):
        print(f"Hello, here is branch {self.name} of {self.bank_name}.")
        
    @staticmethod
    def which_bank():
        print("This is", Bank.bank_name, ".") # staticmethod do not have access to self or cls.
        
    @classmethod # update at class level
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

b1 = Bank("City")
b1.branch()
b1.which_bank()

Bank.change_bank_name("Belief")
b1.branch()