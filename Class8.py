# Flow controls
# conditional statements

# python will work with indent(i.e. space)
# if ,elif,else
x = 3
print(x == 6)

# we have only one condition
if x == 6:
    print("both values are equal")

#  we have two conditions to check
key = 2
if key == 1:
    print("key is belongs to room1")
else:
    print("key is belongs to other room")

#  we have multiple conditions to check
key = 3

if key == 1:
    print("key is belongs to room1")
elif key == 2:
    print("key belongs to room2")
elif key == 3:
    print("key belongs to room3")
elif key == 4:
    print("key belongs to room4")
elif key == 5:
    print("key belongs to room5")
else:
    print("key belongs to room6")

# elif x > 6:
#     print("both values are greater than")
# elif  x >= 4 and x <6:
#     print("value is inbetween 4 and 6")
# else:
#     print("value of x is", x)
y = 7
if y == 7:
    print("y is equal")
    print("I entered into if condition")
else:
    print("not equal y")
