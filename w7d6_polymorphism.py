# Implement Polymorphism (Method Overriding)

class Animal:
    def __init__ (self, name):
        self.name = name
        
    def say(self):
        return "Some sound..."

class Dog(Animal):
    def say(self):
        return 'woof, woof...'
    
class Cat(Animal): 
    def say(self):
        return 'meow, meow...'
    
d1 = Dog("puppy")
c1 = Cat("mimi")

print(d1.say())
print(c1.say())
print(Animal.say("generic animal"))