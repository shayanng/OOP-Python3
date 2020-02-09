# Object oriented programming has 3 main pillars
# 1.Encapsulation 
# 2.Inheritance
# 3.Polymorphism

### in this file i will be foucosing on inheritance & Polymorphism

#%% Inheritance 1
class Date(object):
    def get_date(self):
        return "2014-10-13"
    
class Time(Date):
    def get_time(self):
        return "04:12:09"
        
dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())

#%% Inheritance 2
class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print("%s is eating %s!" % (self.name, food))
        
class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s!" % (self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print("%s shred the string %s!" % (self.name))
        
r = Dog('Rover')
f = Cat('fluffy')

r.fetch("paper")
f.swatstring()
r.eat("dog food")
f.eat("cat food")
r.swatstring()

#%% polymorphism

class Animal(object):
    
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print("{0} eats {1}".format(self.name, food))
        
class dog(Animal):
    
    def fetch(self, thing):
        print("{0} goes after the {1}".format(self.name, thing))
        
    def show_affection(self):
        print("{0} was tail".format(self.name))
        
    








