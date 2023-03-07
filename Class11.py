# while
# it will check for condition before execution of code
x = 1
# if x<6:
#     print("lesser than 6")
while x < 11:
    print("printing x value")
    print(x)
    x += 1  # x = x+1

# reverse number 123
num = 4567
original = num
# 7
# 76
# 765
# 7654
reversenum = 0
while num > 0:
    digit = num % 10
    reversenum = reversenum * 10 + digit
    num //= 10

print(reversenum)

# check two strings are palyndrome
if original == reversenum:
    print("Polyndrome")
else:
    print("not polyndrome")

str1 = "aaabbccdddddddeeffaabbeeffjsfgsdjfhjksdhfjklsgdfkjasshdfkjsahgdkjfsajfgsajdgfjsadgfjsjaddgfjljsgdjfhgasjdfgsjdjdgfjasdgfjljasgdfjdsgjfjgashdj"
# from above string need to find which character is repeated how many times
str1.count("a")
str1.count("b")
dict1 = {}
for i in str1:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1

print(dict1)

# find second-largest element of list with different ways by using inbuilt and without inbuilt
l1 = [1,3,5,6,7,8,8,9,5,9]

l2 =list(set(l1))
# by using inbuilt functions
l2.sort()
print(l2)
# we have to use negative index
print(l2[-2])