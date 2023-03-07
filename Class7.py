# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators

# Arithmetic operators
# Addition(+),Subtraction(-),Divison(/),Multiplication(*),Modulation(%),exponential(**),Floordivision(//)
x = 5
y = 3
print("Add:", x + y)
print("Sub:", x - y)
print("Div:", x / y)
print("Multi:", x * y)
print("Expo :", x ** y)
print("Modula:", x % y)
print("Floordivi:", 1239 // 10)

# Assignment operators
x = 5
x += 2  # it same as x = x+2
print("x+=2 :", x)
x -= 1  # it same as  x = x-1
print("x-=1 :", x)
x *= 3  # it same as x = x*3
print("x*=3 :", x)
x /= 2  # it same as x=x/2
print("x/=2 :", x)
x %= 2  # it same as x = x%2
print("x%=2 :", x)
x **= 3  # it same as x = x**3
print("x**=3 :", x)
x = 1239
x //= 10  # it same as x = x//10
print("x//=3:", x)

# Comparison operator
x=5
y=5
print("equal == :", x==y)
x=5
y=6
print("equal != :", x!=y)
print("greater than != :", y>x)
print("lesser than != :", x<y)

x=10
y=10
print("greate or equal :" , y>=x)

x=10
y=9
print("greate or equal :" , y<=x)

# Logical operator
# and ,or ,not
x = 5
print("and operator :" , x < 8 and x > 4)
# True and True => True
# True and False => False
# False and True => False
# False and False => False
x=5
print("or operator: ", x <5 or x>4)
# True or True => True
# True or false => True
# False or True => True
# False or False => False
# not
print("not operator :" , not(x==5))
print("not operator :" , not(x>5))

# Identity operator
x=5
y =x
z= 6
print("is identity operator:" , x is y)
print("is not identity operator:" , x is not y)

# Membership operator
# in ,not in
l1 = [1,2,3,4]
print("in operator" , 3 in l1)
print("not in operator ", 3 not in l1)



