# Import statement
import random
import string


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

print( ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=10)))