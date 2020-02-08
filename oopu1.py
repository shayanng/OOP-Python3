#%%
mylist = ["a", "b", "c"]
mybool = True
mynone = None

print; print

def my_func():
	print("hello")

print(type(mylist))
print (type(mybool))
print (type(mynone))
print (type(my_func))

this_type = type(mylist)
print(type(this_type))


# %%
class Myclass(object):
	var = 10

this_obj = Myclass()
that_obj = Myclass()
print(this_obj.var)
print(that_obj.var)
# %%
class Joe(object):
	def callme(self):
		print('calling "callme" method with instance: ')
		print(self)
this_joe = Joe()

this_joe.callme()

# %%
import random

class Myclass(object):
	def dothis(self):
		self.rand_val = random.randint(1,10)

my_inst = Myclass()
my_inst.dothis()
print(my_inst.rand_val)

# %%
class My_class(object):
	def set_val(self, val):
		self.value = val
	
	def get_val(self):
		return self.value

a = My_class()
b = My_class()

a.set_val(10)
b.set_val(100)
a.value = 'hello'

print(a.get_val())
print(b.get_val())

# %% Encapsulation
class My_integer(object):
	def set_val(self, val):
		try:
			val = int(val)
		except ValueError:
			return 
		self.val = val

	def get_val(self):
		return self.val
	def increment_val(self):
		self.val = self.val + 1


i = My_integer()
i.set_val(9)
print(i.get_val())
i.set_val('hi')
print(i.get_val())
i.increment_val()

# %%  the __init__ constructor
class MyNum(object):
    def __init__(self):
        print("Calling __init__")
        self.val = 0
        
    def increment(self):
        self.val = self.val + 1

        
        
        
        

        
        
        
        
        
        
        
        
        
        
