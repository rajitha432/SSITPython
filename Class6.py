# tuple
# syntax
t1 = ()

# CRUD
# Create
tuple1 = ("krishna", "sandeep", "lakshmi", "vivek", "raghu", "dilip", "imran", "mohan")

# Read
# with index,slicing
# index => Positive Index,Negative index
print(tuple1[0])
print(tuple1[-5])
print(tuple1[1:5])
print(tuple1[-1:-4:-1])
print(tuple1[0:6:2])
print(tuple1[::-1])
# update
# tuple will not support update
# tuple1[0] ="Krishna M"

# delete
# tuple will not support individual item delete
# del tuple1[0]
# we can delete complete tuple object but not items from in it
del tuple1

# tuple is a constant means its unchangeable/immutable
# only we can read the data from tuple in runtime

# List is a changeable/mutable , means we can change the data, and we can delete the data based on index
# and based on slicing or by using some methods

# In realtime when we have some configurations like application settings, environment settings which can
# not be modified in run time

# mutable => changeable => example : List
# Immutable => not changeable => example : tuple

# list,tuple,set,dictionary
# [],()
# set
# syntax
# CRUD
# Create
set1 = {7, 3, 2, 6, 53, 75, 3, 2}
l1 = [7, 3, 2, 6, 53, 75, 3, 2]
t1 = (7, 3, 2, 6, 53, 75, 3, 2)
print(set1)
print(l1)
print(t1)
# set removes duplicates
# it will not maintain same sequence of order because as it tries to remove duplicates

# Read
# index or slicing will not work for set

# by using loop we can
# print("before loop",set1)
for i in set1:
    print(i)

# print("after loop",set1)
# update
# will not work as index,slicing is not supporting by set

# adding data to set
set1.add(5)
set1.add("Krishna")
# set1.add({"Lakshmi","Sasikala"})
print(set1)
set1.update([10, 9, 5])
print(set1)

# delete
set1.remove(2)
print(set1)
# with index/slicing we can not delete
temp = set1.pop()
print("pop value:", temp)
set1.clear()
print(set1)

#  it has some Mathematical logics
set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6, 7}
# union,intersection,difference

# union => it will merge both sets and removes duplicates
print("union :", set1.union(set2))

# Intersection => it will take common values between two sets
print("Intersection :", set1.intersection(set2))

# difference
print("Difference of set1:", set1.difference(set2))
print("Difference of set2:", set2.difference(set1))

#
l1 = [1, 2, 3, 4, 1, 2, 3]
# we have to do datatype conversion
temp = set(l1)
print(temp)
l2 = [1, 2, 3, 4, 5, 6]
set2 = set(l2)
l3 = temp.intersection(set2)
print("l3: ",l3)
print(type(set2))

# primitive types => string,float,int,bool
# sequence data types => list,tuple,set,dictionary

# dictionary => it's a key and value pair
# [],(),{}
# syntax
dict1 = {}
print("dict1" ,type(dict1))
banknames = ["sbi","icici","canara"]
bankdetails = ["chandra",13345666,"SBI",7887,87777]
print(bankdetails)
bankdetails = {"AccountName":"Chandra","AccountNumber":13345666,"BankName":"SBI","Balance":7887}

print(bankdetails)
# CRUD
# Create
bankdetails = {"AccountName":"Chandra","AccountNumber":13345666,"BankName":"SBI","Balance":7887,"Balance":9876}
print(bankdetails)
#  the key in dictionary can not be duplicate
# Read
# we need to access with key
print(bankdetails["AccountName"])
print(bankdetails.keys())
print(list(bankdetails.keys()))
print(bankdetails.values())
print(bankdetails.items())

# update
# we can not update the keys once its defined , keys are immutable
# we can  update only values
# how we will update value based on key
bankdetails["AccountNumber"] = 987654
bankdetails["BankName"] ="icici"
print(bankdetails)

# how to add data to dictionary
bankdetails["bankName"] = "hdfc"
bankdetails["address"] = "ATP"
print(bankdetails)

# delete
del bankdetails["Balance"]
print(bankdetails)
# del bankdetails # it will delete complete dictionary object from memory
#
bankdetails.clear()
print("after clear :" , bankdetails)

dict2 = {"AccountName":"Chandra","AccountNumber":13345666,"BankName":"SBI","Balance":7887}
temp = dict2.pop("AccountName")
print("pop return :",temp)
print("after pop:",dict2)

dict2.update({"AccountNumber":56777,"BankName":"ICICI","Address":"ATP"})
print(dict2)

# what are the datatypes can we used as keys
# string,int,tuple
dict3 ={1:"Chandra",2:"Krishna",3:"Sandeep",4:["vani","Veena","Vivek"],5:{"name":"chandra","id":1244}}

print(dict3)
dict4 = {(1,2,3):"names"}
print(dict4)

print(dict3[4][1])
print(dict3[5]["id"])

# list,tuple,set,dictionary
















