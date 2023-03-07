# oops

# bank

# account details
# savings account
# current account
# personal loan
# vehicle loan

# oops => object-oriented programming structure
# class,object,abstraction,encapsulation,polymorphism,inheritance

# Class => class is a container , which contain member variables/members and member functions

class bank:

    bank_location = "MUM"
    def __init__(self,name,address):
        self.bank_name = name
        self.bank_address = address
        print("I am in bank constructor")

    def savings_account(self,account_number):

        print("from savings account :",account_number)

    def current_account(self,accountnumber):
        print("from current account",accountnumber)

    def vehicle_loan(self):
        print("from vehicle loan")


#  object => it's instance of a class
objbank = bank("hdfc","ATP")
print(objbank.bank_name)
objbank.bank_name ="ICICI"
objbank.savings_account(34455545)
print(objbank.bank_name)
print(objbank.bank_address)
objbank.current_account(564556455)
objbank.vehicle_loan()
print("/////////////Class variable accessing without object/////////")
print(bank.bank_location)


# self => it represents current instance of class
# Class variable =>  variable which is declared in class level , this can be accessed without object
# instance variable => variable which is attached to self(i.e. attached to object)
# constructor => which is used to construct an object , this is the initial place which will be called
# while creating object

# special/magic methods => these are inbuilt methods which will start with __ and ends with __(double underscore)



