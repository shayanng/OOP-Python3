import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@dreamber.com"
    
    def full_name(self):
        print("{} {}".format(self.first, self.last))

emp_1 = Employee("Sam", "Morin", 50_000)
emp_2 = Employee("Helen", "Shiri", 50_000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print("{} {}".format(emp_1.first, emp_1.last))
print("{} {}".format(emp_2.first, emp_2.last))