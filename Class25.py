# Variables,Datatypes(string,int,float,bool,list,tuple,set,dictionary),Indexing,slicing,negative indexing
# typecasting
# operators(Ar-thematic ,assignment,comparison,logical,identity,membership)
# conditional statements (if,elif,else)
# loops(for loop,while)
# range
# functions
# scopes =>local/global
# types of arguments in functions(positional,default,keyword,arbitrary ,keyword arbitrary)
# break,continue,pass,yield
# return
# inner function
# decorator
# closure function
# MRO
# iterator,generator
# multipleddispatch
# exception handling => try except finally
# oops (class,object,abstraction,encapsulation,polymorphism,inheritance)
# file handling
# regex

# lambda function,filter,map,reduce
# lambda => its anonymous function(function which will not have any name) or inline function

def multiplication(x):
    return x * 2

print("/////lambda/////////")
y = lambda x: x * 2
print(y(5))
# filter => it applies some condition on data
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, l1))
print(even_numbers)
# map => it will iterate through the data and applies some logic
total_numbers = list(map(lambda x:x*2,l1))
print(total_numbers)
# reduce
total =0
for i in l1:
    total+=i

import functools
# i want calculate sum
total = functools.reduce(lambda a,b:a+b,l1)
print("reduce  :",total)
mx_value = functools.reduce(lambda a,b: a if a>b else b,l1)
print(mx_value)

mx=0
for i in l1:
    if i > mx:
        mx= i
print(mx)

# Big data (Python)
# Development(Python)=> web applications,api development
# AI,Machine learning
# Automation Development/Testing => Testing
# Automation Testing(Python)

# Testing => Manual Testing
# Tester => he/she has to verify application is working or not
# will create bug by giving explanation

# Automation Testing => Python
# we will write code to test the code which has been developed by developers
# Acceptance criteria => will be developed by Product owner(PO), business analyst(BA)

# Positive
# Negative
# Lower boundary
# Upper boundary


