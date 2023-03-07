# file handling
file1 = open("practice.txt","w")
file1.write("Hello guys welcome")
file1.close()

file2 = open("practice.txt","r")
data = file2.read()
print(data)
file2.close()

# context management => it will dispose the object once we come out of the particular context/block of code
with open("practice.txt","w+") as file3:
    file3.write("writing and reading both operations")
    data = file3.read()
    print(data)
with open("practice.txt","r") as file3:
    data = file3.read()
    print(data)

# modes => write , read,append,read+,write+
with open("practice.txt","r+") as file3:
    data = file3.read()
    file3.write("testing write from read mode")
    print(data)

with open("practice2.txt","a") as file3:
    data = file3.write("added new python version 3.10")
    print(data)

# regular expressions
print("///////regular expression///////////////")
import re
str1 = 'hey how are you how is the things are goin on'
pattern = re.compile(r'\bhow\b')
data = re.findall(pattern,str1)
print(data)
data1 = re.match(pattern,str1)
print(data1)

pattern = '^a....s$'
test_string = 'abydfs'
result = re.match(pattern, test_string)
if result:
    print("matched")

ippattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
str2 ="hi i am connnecting from 10.23.56.3 and 44.55 and sending data to 34.54.64.34"
print(re.findall(ippattern,str2))

