# Data types
# string,int,float,bool

# string => any data which defined between quotes
name = 'chandraff233'
name1 = "mohan"
print(type(name))

# int => it stores numeric values
age = 24
print(type(age))

# float => it stores decimal values
balance = 343.23
print(type(balance))

# bool => which stores true or false
isvalid = True
is_not_valid = False
print(type(isvalid))


# string inbuilt methods
name ='chandra mohan'
print(name)
# to make first letter as capital
print(name.capitalize())
#  to make upper case
print(name.upper())
# to make lower case
print(name.lower())

# to check whether string is upper or lower
name='CHAN'
print(name.isupper())
# to check whether string is lower
print(name.islower())

# isdigit
age = '23asa'
print(age.isdigit())

# count => to check the characters count
print(name.count('C'))

print("I have done changes from my local branch")