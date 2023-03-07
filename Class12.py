# print even numbers 1 to 10

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in range(50, 100):
    if i % 2 == 0:
        print(i)

for i in range(200, 300):
    if i % 2 == 0:
        print(i)

x = 4
y = 5
x + y

x = 7
y = 8
x + y

l1 = ["krishna", "dilip", "vani", "rajitha", "vishnu"]
for i in l1:
    if i == "krishna":
        print("available")

for i in l1:
    if i == "dilip":
        print("available")


# functions
# a piece of code which can be reusable

# the keyword for function is def
# how to create function
def sample():
    print("hello guys")


# how to call function
sample()


# without parameter

# with parameter
def myname(name,address):
    print("my details are : ", name ," " ,"Address :",address)

myname("chandra",None)
myname("krishna",x)
myname("dilip",y)

