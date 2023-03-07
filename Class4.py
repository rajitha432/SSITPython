# Sequence data types
# list , tuple,set,dictionary

name = "hdfc"
address = "ATP"
ifsccode = "HDFC0003"
balance = 88877666
interest_rate = 10.3
isavailable = True

# list => its combination of different datatypes of data

bank_details = ["hdfc", 9777]
bank_details = [name, address, ifsccode, balance, "5566", "AP"]
print(type(bank_details))
print(bank_details)

# CRUD => Create , Read , update ,Delete
# Create
bank_details = [name, address, ifsccode, balance, "5566", "AP"]

# Read
# Indexing , Slicing
# Indexing
# Reading based on index
# Positive Indexing
print(bank_details[0])
print(bank_details[3])
print(bank_details[5])
# Negative Indexing
print(bank_details[-4])
print(bank_details[-2])
print(bank_details[-6])

# to find the total elements count/length of list
print(len(bank_details))

# find the last element with positive indexing
length = len(bank_details)
print(bank_details[length - 1])
print(bank_details[length - 2])
print(bank_details[length - 3])

# find the last element with negative indexing
print("////////////////Negative indexing///////")
print(length)
print(bank_details[-length])
print(bank_details[-(length - 1)])

# slicing
# start index => from where we need to start
# end index  => where we need to end (it will consider the provided index -1)
# step size => by default value is 1 , how we need to jump to collect data

l1 = ["krishna", "sandeep", "lakshmi", "vivek", "raghu", "dilip", "imran", "mohan"]

print(l1[2])
print(l1[-4])
# slicing syntax => l1[startinex:endindex:stepsize]
print(l1[0:4:1])
print(l1[4:6:1])
# by default step size will be one , so we don't need to define 1
print(l1[4:6:])
# default value for start index will be 0
# default value for end index will be length -1
print(l1[:6])
print(l1[2:])
print(l1[::])

# different step size
print(l1[1:7:2])  # sandeep,vivek,dilip
print(l1[1:7:3])  # 3 =>sandeep,raghu

print("l1[4:3]", ": ", l1[4:5])  # end index should be greater than start index otherwise
# it will give empty result

# slicing with negative indexing
l1 = ["krishna", "sandeep", "lakshmi", "vivek", "raghu", "dilip", "imran", "mohan"]

print("l1[-4:-6]: ",l1[-4:-6])
print("l1[-7:-4:1] :", l1[-7:-4:1]) # sandeep,lakshmi,vivek
print("l1[-3::] :",l1[-3::]) #d,I,m
print("l1[-3:-4] :",l1[-3:-4]) # []
print("l1[-3:-3]):",l1[-3:-3]) # []
print("l1[-1:-5] :",l1[-1:-5]) # []

