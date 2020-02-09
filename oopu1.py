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
    def __init__(self, value):
        print("Calling __init__")
        self.val = value
        
    def increment(self):
        self.val = self.val + 1

dd = MyNum(5)
dd.increment()
dd.increment()
print(dd.val)

#%% the __init__ constructor + try, except
class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value
        
    def increment(self):
        self.val = self.val + 1
        
aa = MyNum("hello")
dd = MyNum(5)
dd.increment()
dd.increment()
print(dd.val)
print(aa.val)

#%% Class Atributes 1
class YourClass(object):
    classy = 10
    
    def set_val(self):
        self.insty = 100
        
dd = YourClass()

dd.set_val()
print(dd.classy)
print(dd.insty)

#%% Class Atributes 2        
class YourClass(object):
    classy = "class value!"
    
dd = YourClass()

print(dd.classy)

dd.classy = "inst value!"

print(dd.classy)

del dd.classy

print(dd.classy)
    
#%% class and instance data
class InstanceCounter(object):
    count = 0
    
    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1
        
    def set_val(self, newval):
        self.val = newval
        
    def get_val(self):
        return self.val
    
    def get_count(self):
        return InstanceCounter.count
    
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print("val of obj: %s" % (obj.get_val()))
    print("count: %s" % (obj.get_count()))    
        
#%% assignment 1
class MaxSizeList(object):
    
    def __init__(self, max):
        self.max_size = max
        self.innerlist = []
        
    def push(self, obj):
        self.innerlist.append(obj)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop(0)
            
    def get_list(self):
        return self.innerlist
    
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")
        
print(a.get_list())
print(b.get_list())        
        
        
        
