# Iterator
l1 =[1,2,3,4,5]

iter1 = iter(l1)
try:
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
except StopIteration:
    print("stop iteration")

# Exception handling

# Generator
def sample():
    return 1
    x=10
    print(x)

sample()

# yield => it will throw the data and proceed for further execution
# return => it will return back from the function one time and can not proceed further execution
# break => it will break the iteration

def samplegenerator():
    yield [1,2,4]
    yield 2
    yield "hello"
    yield 45.7


x = samplegenerator()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for i in samplegenerator():
    print(i)

print("/////////")
def generator():
    for i in range(1,10):
        yield i
x = generator()
print(next(x))
print(next(x))
print(next(x))

for i in generator():
    print(i)