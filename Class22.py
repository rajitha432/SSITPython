# Polymorphism
# over loading => defining same function with different signature in same class
# overriding => Parent and child relation where child can override the functionality

from multipledispatch import dispatch
class calculator:

    @dispatch(int, int)
    def add(self, x, y):
        return x + y

    @dispatch(int, int, int)
    def add(self, x, y, z):
        return x + y + z

    def multipication(self, *args):
        total = 1
        for i in args:
            total *= i
        return total

# MRO => method resolution order , it will take the last defined function
obj = calculator()
print(obj.add(3, 4))
print(obj.add(4, 5, 6))
print(obj.multipication(3,4))
print(obj.multipication(6,5,5))
# is python supports polymorphism by default in python => it will not support overloading , it will support
# overriding
# how will achieve overloading => by using *args,**kwargs, multipleddispatch


# class,object,self,constructor,instancevariable,classvariable,abstraction,encapsulation,polymorphism
# Inheritance => Parent and child relation where child can access the complete parent functionalities
# and child can extend or override
print("///////////Inheritance///////")
class Father:
    def get_house(self):
        print("2 floor building from father")
    def get_commercial_building(self):
        return "4 floor building from father"

class Child(Father):
    def get_lands(self):
        print("1 plot from child")
    def get_commercial_building(self):
        aa = super().get_commercial_building()
        print(aa)
        print("changed to 6 floors building from child")


# to access parent method from child we use key word called super()

child_obj= Child()
child_obj.get_house()
child_obj.get_lands()
child_obj.get_commercial_building()

# How many types inheritance
# Single level inheritance => single relation between father and child
# Multilevel Inheritance
# Multiple Inheritance
# Hierarchical inheritance
print("/////////multilevel////////")
# Multi level
class grandfather:
    def get_agricultre_land(self):
        print("From grandfather 5acres land")

class father(grandfather):
    def get_agricultre_land(self):
        super().get_agricultre_land()
        print("from father changed to 7acre land")
    def get_house(self):
        print("house from father")

class child(father):
    def get_agricultre_land(self):
        super().get_agricultre_land()
        print("from child 4 acre land")

child_obj = child()
child_obj.get_agricultre_land()
child_obj.get_house()
print("///////////Multiple inheritance/////")
# Multiple
class father:
    def get_vehicle(self):
        print("BMW car from father")

class mother:
    def get_glod(self):
        print("gold from mother")
    def get_vehicle(self):
        print("Benz car from mother")

class child(father,mother):
    def get_vehicle(self):
        mother.get_vehicle(self)
        father.get_vehicle(self)


child_obj = child()
child_obj.get_glod()
child_obj.get_vehicle()

# MRO => it will the first class defined in inheritance

# Hierarchical inheritance
class parent:
    def properties(self):
        print("parent properties")

class child1(parent):
    def __del__(self):
        print("destruct complex objects")
        print("I am calling destructor")

class child2(parent):
    pass

ch1_obj = child1()
# del ch1_obj
ch2_obj = child2()
ch1_obj.properties()
ch2_obj.properties()

# isinstance , issubclass
print(isinstance(ch1_obj,child1))
print(isinstance(ch2_obj,child1))
# isinstance => we are just checking which class instance is this
print(issubclass(child1,parent))
print(issubclass(parent,child1))

# destructor => this is called when object is removed from memory , if we want to dispose any objects
# explicitly we can call this
del ch1_obj

# class =>self,class variables,instance variables,__init__(constructor),
# __del__(destructor),class method,instance method,static method, super
# object => isinstance,issubclass
# abstraction
# encapsulation
# polymorphism =>overloading ,overriding
# Inheritance => single,multilevel,multiple,hierarchical



