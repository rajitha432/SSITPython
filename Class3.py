# Data type conversion
# converting from one data type to other
# Implicit
# Explict

# Implicit => the system/python will automatically convert the data type from one
# data type to other/lower to higher data type

balance = 233
interest = 345.56
total = balance + interest
print(total)
print(type(total))

# Explicit => convert from one data type to other explicitly
total = balance + int(interest)
print(total)
print(type(total))

name = 'chandra'
address = "23,Ram Nagar,ATP"
pincode = 515001
# converting pincode from int to string
complete_address = name + "\n" + address + " " + str(pincode)
print(complete_address)

amount = 35
loan_amount = "566"
# converting loan_amount from string to int
total_loan = amount + int(loan_amount)
print(total_loan)

# Primitive Data type => string,int,float,bool
# Sequence data type/data structures => list,tuple,set,dictionary
