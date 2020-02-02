#Employee class Credit to: Corey Schafer Youtube Channel ~~
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.035
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@dreamber.com"
        
        Employee.num_of_emps += 1
    
    def full_name(self):
        print("{} {}".format(self.first, self.last))
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Sam", "Morin", 50_000)
emp_2 = Employee("Helen", "Shiri", 50_000)

#print(emp_1)
#print(emp_2)

#print(emp_1.email)
#print(emp_2.email)

print(emp_1.full_name())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.__dict__)

emp_1.raise_amount = 1.047

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)

