# Create an Employee Class (Using Inheritance)

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_info(self):
        return f"Employee ID: {self.id}\nEmployee Name: {self.name}"
    
class Manager(Employee):
    def __init__(self, id, name, level):
        super().__init__(id,name)
        self.level = level
    
    def get_level(self):
        return f"{self.name} is level {self.level}."
        
e1 = Employee(1, 'James Smith')
print(e1.get_info())

m1 = Manager(2, 'Dollar R', 4)
print(m1.get_info())
print(m1.get_level())

print(Manager.get_info(m1))