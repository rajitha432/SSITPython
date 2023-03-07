# return

aadhardetails=[]
def createaadhardetails(name, aadharnumber, address, state="DL", country="INDIA"):
    aadhar = {"name": name, "aadharnumber": aadharnumber, "address": address, "state": state, "country": country}
    aadhardetails.append(aadhar)


createaadhardetails("Lakshmi", 987777, "ATP", "AP", "USA")
createaadhardetails("Mohan", 87777, "ATP")

print(aadhardetails)
def get_aadhar_details(aadharnum,name):
    for i in aadhardetails:
       if i["aadharnumber"] == aadharnum and i["name"] == name :
            return [i]

    return "Aadhar details not found"


details = get_aadhar_details(87777,"Mohan")
print(details)
details1 = get_aadhar_details(99999,"aa")
print(details1)
# what is the by default return type => None


def sample():

    return "hi"
    print("after return")

print("I am from outside")

x = sample()
print(x)
print(sample())

# what is the difference between break,continue,return
# break => it will be used only in the iteration, and it will break the iteration
# continue => it will be used only in the iteration, and it will skip the current iteration
# return => it can be used in function without iteration also, and it will take back some data

print("/////////Function inside function //////")
# function inside function
def outerfunction():
    def innerfunction(x,y):
        print("I am from inside",x+y)

    # innerfunction()
    print("I am from outside")
    return innerfunction



temp = outerfunction()
# print(x)
temp(2,3)