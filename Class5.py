l1 = ["krishna", "sandeep", "lakshmi", "vivek", "raghu", "dilip", "imran", "mohan"]

# Negative step size
print(l1[2:6:1])
print(l1[2:6:2])  # l,r
print(l1[6:2:-1])  # l,v,r,d
print(l1[6:2:-2])  # i,r

# Positive Indexing,Negative Indexing,Slicing(Start index,end index,stepsize)

# List
# CRUD
# Create
# Read => Indexing,Slicing

# Update
name = l1[0]
print(name)
l1[0] = "Krishna Murthy"
print(l1[0])
print(l1)

l1[-1] = "Mohan M"
print(l1)
# update with slicing
print(l1[2:4])
l1[2:4] = ["Lakshmi L", "Vivek V", "Chandra", "Nandu"]
print(l1)

# delete
del l1[0]
print(l1)
del l1[2:6:2]
print(l1)
l1.clear()
# del l1
# print(l1)

# Methods in list
# to insert records we have two methods , i.e. append,extend
l2 = ["hdfc", "sbi", "icici"]
# append => to add single record into list we need to use append
l2.append("Union")
l2.append(["Canara", "axis"])

print(l2)
print(l2[4])
print(l2[4][1])
# extended
l2.extend(["RBI", "Baroda"])
print(l2)
l2.extend("Andhra Bank")
print(l2)

# methods to delete
l2.remove("hdfc")
print(l2)
temp = l2.pop()
print(temp)
print(l2)
temp = l2.pop(1)
print(temp)
print(l2)

# some more methods
l2.append("sbi")
print(l2)
print(l2.count("sbi"))

l2.insert(2,"Grameena")
print(l2)

l2.pop()
print(l2)
l2.reverse()
print(l2)

# sort the data
l3 =[5,2,5,6,4,8]
l3.sort()
print(l3)

l4 = [["a","c"],["a","b","a","d"]]
l4.sort()
print(l4)

# del l2[-4]
# l2.sort()
# print(l2)


l5 =[]
for i in l2:
    if type(i) is not list:
        l5.append(i)

print(l5)        