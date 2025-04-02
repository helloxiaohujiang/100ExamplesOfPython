# Create a Class for a Shopping Cart

class ShoppingCart:
    def __init__(self):
        self.shopper = "Jim Green"
        self.item = 0
        self.balance = 0
    
    def add_item(self, to_add, to_add_price):
        self.item += to_add
        self.balance += to_add_price
        return "{} items selected, price ${:.2f}".format(self.item, self.balance)
        
    def sub_item(self, to_sub, to_sub_price):
        if to_sub > self.item:
            return "Error: Cannot remove more items than available."
        if to_sub_price > self.balance:
            return "Error: Cannot subtract more balance than available."
        self.item -= to_sub
        self.balance -= to_sub_price
        return "{} items remaining".format(self.item)
        
    def check_out(self):
        return "There are {} total items selected. You need to pay ${:.2f}.".format(self.item, self.balance)
          

p1 = ShoppingCart()
print(p1.add_item(2,200))
print(p1.sub_item(1,100))
print(p1.check_out())