# scope
# global scope
# local scope

x = 10  # global scope


def samplescope():
    global x
    x = 20
    global y
    y = 30  # we made it as global scope by using global keyword
    z = 40
    print("x from function", x)
    print("y from function", y)


# the local changes/scope wants to reflect to outside
# we have keyword called global we can give access to outside

samplescope()
print("x from outside", x)
print("y from outside ", y)

# how many types of parameters/arguments
# Positional arguments
# keyword arguments
# default arguments
# arbitrary arguments (args)
# keyword arbitrary arguments (kwargs)

# positional arguments

customers = []


def bankdetails(name, accountnumber, bankname, ifsccode):
    customer = {"name": name, "accnumber": accountnumber, "bank": bankname, "ifsc": ifsccode}
    customers.append(customer)


bankdetails("Ram", 3553553, "hdfc", "hdfc0002")
bankdetails(656565, "hari", "hdfc", "hdfc004")
print(customers)
print(len(customers))
# Irrespective of the data it will pass/assign in a same order which parameters are defined

# keyword arguments
bankdetails(bankname="hdfc", name="chandra", accountnumber=355353, ifsccode=9877)
print(customers)
bankdetails("phani", 90233298, bankname="hdfc", ifsccode=9888)
print(customers)

print("////////Default arguments////")
# default arguments
aadhardetails = []


def createaadhardetails(name, aadharnumber, address, state="DL", country="INDIA"):
    aadhar = {"name": name, "aadharnumber": aadharnumber, "address": address, "state": state, "country": country}
    aadhardetails.append(aadhar)


createaadhardetails("Lakshmi", 987777, "ATP", "AP", "USA")
createaadhardetails("Mohan", 87777, "ATP")
print(aadhardetails)

print("//////////arbitrary arguments/////////")


def add(x, y):
    print(x + y)


add(3, 4)


def addition(*args):
    total = 0
    for i in args:
        total += i  # total = total +i

    print("sum of ", args, " :", total)


addition(2)
addition(2, 3)
addition(2, 3, 4)
addition(2, 3, 4, 5)
addition(4, 5, 6, 7, 7)
addition()

print("///////keyword arbitrary arguments////")
# key word arbitrary arguments
def customerdetails(**kwargs):
    print(kwargs)
    for i in kwargs:
        print("Value for ",i,":",kwargs[i])

customerdetails()
print("//////////")
# customerdetails(name="python")
customerdetails(name="test",id=23345)

# the order of passing arguments
print("/////Combination of all arguments types//////")
def sample(name,id,address="ATP",*args,**kwargs):
    print(name," ",id," ",address," ",args," ",kwargs)

sample("chandra",13333)
sample("chandra",2333,55)
sample("chandra",1333,1,2,3)
# Positional, default, arbitrary , keyword arbitrary

