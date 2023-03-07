# abstraction,encapsulation

# abstraction
class bank:

    def chek_balance(self):
        return "balance amount is 1000"

    def withdraw_cash(self,customerid,amount):
        customerdetails = [{"name":"chandra","cusid":45666,"balance":35555},
                           {"name":"lakshmi","cusid":98778,"balance":40000},
                           {"name":"rajitha","cusid":4455,"balance":50000}]
        for item in customerdetails:
            if item["cusid"] == customerid:
                if item["balance"] >= amount:
                    return "withdrawing amount"
                else:
                    return "no sufficient balanace to withdraw"



obj_bank = bank()
obj_bank.withdraw_cash(4455,10000)

# abstraction => exposing the details to outside world


class ATM:

    def __init__(self,atmcardnumber,pin):
        self.__atmpin = pin
        self.__cardnumber = atmcardnumber

    def __vlidate_customerdetails(self):
        if self.__atmpin==1245 and self.__cardnumber==4645345453:
            return True
        else:
            return False

    def withdraw(self,amount,customerid):
        if self.__vlidate_customerdetails():
            obj_bank = bank()
            obj_bank.withdraw_cash(amount,customerid)
        else:
            return "Not a valid crederntials"

# encapsulation => hiding the details , nothing but hiding the members and member information/member function
# by making them as private , in python we will make it as private by using __(double underscore)

obj_atm = ATM(8877888777,3455)
obj_atm.withdraw(1000,334555)

# polymorphism
# poly => many
# morphism => forms/ways

# polymorphism => defining same function with different signature
# over loading ,overriding
# MRO => method resolution order
from multipledispatch import dispatch

def add(x,y):
    return x+y

def add(x,y,z):
    return x+y+z

add(2,3,5)
add(4,5,6)

def add(*args):
    total =0
    for i in args:
        total+=i
    return total

add(2)
add(3,4)
add(5,6,7)

def addition(**kwargs):
    total = 0
    for i in kwargs:
       total += kwargs[i]
    return total

addition(x=4,y=5,z=7)
addition(a=5,b=6)


