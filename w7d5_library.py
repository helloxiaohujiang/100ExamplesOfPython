# Create a Class for a Library Management System

class Library:
    name = 'Subiaco'
    
    @staticmethod
    def get_lib_info():
        return f"Hello, welcome to {Library.name} library!"
    
    def __init__(self, open_time, close_time):
        self.open_time = open_time
        self.close_time = close_time

    def open_door(self):
        return f"Open door at: {self.open_time}"
    
    def close_door(self):
        return f"Close door at: {self.close_time}"
    
class Book(Library):
    def __init__(self, open_time, close_time, available_amount, borrow_amount):
        super().__init__(open_time, close_time)
        self.avialable_amount = available_amount
        self.borrow_amount = borrow_amount

    def borrow_book(self):
        if self.borrow_amount <= self.avialable_amount:
            self.avialable_amount -= self.borrow_amount
            return f"Congrats, you have borrowed {self.borrow_amount} books."
        else:
            return (f"Sorry, not enough books available." 
                    f"Only {self.avialable_amount} left. See you next time!")
    
    def back_book(self,returned_book):
        self.avialable_amount += returned_book
        
        return f"Thank you for returning, now we have {self.avialable_amount} books available."
    
    @classmethod
    def update_lib_info(cls,name):
        Library.name = name
    
l1 = Library("8:00AM", "4:00PM")
print(l1.open_door())
print(l1.close_door())

b1 = Book("8:00AM", "4:00PM", 20, 2)
print(b1.open_door())
print(b1.close_door())
print(b1.borrow_book())
print(b1.back_book(1))

print(b1.get_lib_info())
b1.update_lib_info('Claremont')
print(b1.get_lib_info())