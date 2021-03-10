#assertion
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price
shoes = {'name': 'Fancy Shoes', 'price': 14900}

print(apply_discount(shoes,0))


#Also the leading _ single underscore is used to avoid Wildcard imports from package
#  from Abc import *
#  import Abc
# suppose _myAbc() was there in the Abc module
#so _myAbc() wont work in first case but Abc._myAbc() will work in second case

#__ leading double underscore is used to mimic the private concept in java
# the var cna be used through the method only 
class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'
    def get_mangled(self):
        return self.__mangled
Obj=ManglingTest()
print(Obj.get_mangled())


name="farman"
errno=12345
#1
print('Hey %s, there is a 0x%x error!' % (name,errno))
print('Hey %(nam)s, there is a 0x%(err)x error!' % {"nam":name,"err":errno})
#2
print(f'Hey {name}, there is a 0x{errno:x} error!')
#3
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name,errno=errno))
#4
from string import Template
t=Template('Hello $namee')
t=t.substitute(namee=name)
print(t)

#map
print(list(map(lambda x: x.upper(),['hi','hello'])))

#sort vs sorted
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
tuples.sort(key=lambda x: x[0])
print(tuples)

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
t=sorted(tuples,key=lambda x: x[1])
print(t)

#decorator 1
def my_multiplier(a,b,c):
    return a*b*c

def decorated_my_multiplier(func):
    def inside(a,b,c):
        print('{} * {} * {}.'.format(a,b,c))
        return func(a,b,c)
    return inside

my_multiplier=decorated_my_multiplier(my_multiplier)
print(my_multiplier(2,3,4))

#decorator 2
import functools
def decorated_my_adder(func):
    @functools.wraps(func)#to not loose the docs of func argument
    def inside(a,b,c):
        print('{} + {} + {}.'.format(a,b,c))
        return func(a,b,c)
    return inside

@decorated_my_adder
def my_adder(a,b,c):
    return a+b+c

print(my_adder(2,3,4))


#argument unpacking at function call
def print_vector(x, y,z):
    print('<%s, %s, %s>' % (x, y, z))
              
tuple_vec = (1, 0, 1)
list_vec = [1, 0,2]
print_vector(*tuple_vec)
print_vector(*list_vec)

#also kwargs can be unpacked
dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(**dict_vec)

#note
print_vector(*dict_vec)

#Shallow copy: The outer layer gets copied and any
#any change on complex data inside it is changed then
#that is also reflected in the main one but if scalars are changed in
#the shallow copy the value is not changed in the main

#implementing java like abstract class mechanism
from abc import ABCMeta, abstractmethod    
class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass
class Concrete(Base):
    def foo(self):
        return 'foo() called'

    def bar(self):
        return 'bar() called'

B=Concrete()
print(B.bar())

# repeater and iterator to explai how python loop works
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
        return self.source.value
    
class Repeater():
    def __init__(self,value):
        self.value=value
        
    def __iter__(self):
        return RepeaterIterator(self)
#or

class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value 
#repeater = Repeater('Hello')
#for item in repeater:
    #print(item)

#or
#repeater=Repeater('Hi')
#i=repeater.__iter__()
#while True:
    #item=i.__next__()
    #print(item)

