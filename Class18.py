# exception handling
# try ,except,finally
try:
    pass
except:
    pass
finally:
    pass

# try block contains the code/logic from which we are expecting exception
# except block will execute when ever there is an exception occured in try block, we can see exception here
# we can print or log the exception
# finally => this will execute whether exception occurs or not

import logging

list1 = []
logging.basicConfig(filename='sample.log',format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
try:
    name = "chandra"
    temp = name.upper()
    print(temp)
    list1=['chandra', 'nanda']
    name = 'None'
    name.upper()
    print(name)
    10/0
except Exception as ex:
    print("error occured",ex)
    logger.debug(ex)
finally:
     list1.clear()

balance = "2344"
principal = 344
total = int(balance) + principal

# strings are anagram
def sortlist(l1):
    for i in range(len(l1)-1):
        for j in range(i+1,len(l1)):
            if l1[i] > l1[j]:
                l1[i] ,l1[j] = l1[j],l1[i]
    return l1

def checkanagram(str1,str2):
    if len(str1) == len(str2):
        position = 0
        matches = True
        l1 = (list(str1)).sort()
        l2 = sortlist(list(str2))

        while position < len(str1) and matches:
            if l1[position] == l2[position]:
                position = position+1
            else:
                matches = False
        return  matches


if checkanagram("silent","listen"):
    print("anagram")
else:
    print("not anagram")







