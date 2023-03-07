# MRO,Decorator,Iterator,Generator
# MRO => method resolution order

def add(x,y):
    return x+y

def add(x,y,z):
    return x+y+z

def add(x):
    return x

add(2)
add(3)

# multipleddispatch
from multipledispatch import dispatch

@dispatch(int,int)
def sub(x,y):
    return x-y

@dispatch(int,int,int)
def sub(x,y,z):
    return x-y-z


print(sub(4,3))
print(sub(7,3,1))

# *args ,*kwargs

def addition(*args):
    total=0
    for i in args:
        total+=i
    return total


print(addition(4))
print(addition(4,5,6.7))
print(addition(21.44,67.55))

print("////////Decorator//////////")
# Decorator

def calculator(funct1):
    def inner1(a,b):
        print("Executing from decorator")
        if a>0 and b>0 :
           result = funct1(a,b)
           print("received result from divison function ",result)
        else:
            print("input values should be greater than 0")
    return inner1

@calculator
def division(x,y):
    return x/y

division(3,2)
division(2,0)

print("///////closure function////")
# closure function
def outerfunction(z):
    def innerfunction(x,y):
        print("I am from inside",x+y+z)

    # innerfunction()
    print("I am from outside")
    return innerfunction



temp = outerfunction(6)
# print(x)
temp(2,3)

# closure function => The inner function holds the references of parameters even though the outer function is closed
