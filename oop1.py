import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@dreamber.com"

emp_1 = Employee(Sam, Morin, 50_000)
emp_2 = Employee(Helen, Shiri, 50_000)

print(emp_1)
print(emp_2)

emp_1.first = "Sam"
emp_1.last = "Morin"
emp_1.email = "sam.morin@dreamber.com"
emp_1.pay = 50_000


emp_2.first = "Test"
emp_2.last = "Tester"
emp_2.email = "test.tester@dreamber.com"
emp_2.pay = 60_000

print(emp_1.email)
print(emp_2.email)

