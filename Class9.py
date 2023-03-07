# Loops => for , while
l1 = ["chandra", "krishna", "nandu", "vivek", "vani", "rajitha", "sandeep"]
# x = l1[0]
# print(x)
# x = l1[1]
# print(x)
# loop is nothing but iteration
# loop syntax
for item in l1:
    print(item)

dict1 = {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
         "avatar": "https://reqres.in/img/faces/7-image.jpg"}

print("//////////")
for i in dict1.keys():
    print(dict1[i])

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("//////////")

for i in l1:
    if i % 2 == 0:
        print("even number - ", i)
    else:
        print("odd number - ", i)

data = [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
         "avatar": "https://reqres.in/img/faces/7-image.jpg"},
        {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
         "avatar": "https://reqres.in/img/faces/8-image.jpg"},
        {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
         "avatar": "https://reqres.in/img/faces/9-image.jpg"},
        {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
         "avatar": "https://reqres.in/img/faces/10-image.jpg"},
        {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
         "avatar": "https://reqres.in/img/faces/11-image.jpg"},
        {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
         "avatar": "https://reqres.in/img/faces/12-image.jpg"}]

# first_name - byron
for i in data:
    if i["first_name"] == "George":
        print(i)

l1 = [{"Aadharnumber": 233333, "Name": "Dilip"}, {"Aadharnumber": 9777677, "Name": "Krishna"},
      {"Aadharnumber": 7766766, "Name": "Krishna"}]
for i in l1:
    if i["Aadharnumber"] == 9777677:
        print(i)

# range => start index , end index ,stepsize
# end index => it will always take provided value -1

for i in range(2, 100):
    print(i, end=" ")

# print("")
print("hello")

l1 = ["chandra", "krishna", "nandu", "vivek", "vani", "rajitha", "sandeep"]

print("///////")
for i in range(0, len(l1)):
    print(l1[i], end=" ")

print("")

for i in range(0, len(l1)):
    if l1[i] == "chandra":
        l1[i] = "Chandra R"

print(l1)

# Print even numbers between 50 to 100
for i in range(50, 101, 2):
    if i % 2 == 0:
        print(i, end=',')

str1 = "hello python"
print("")
for i in str1:
    print(i)

print("/////////")
# reverse string
output = ''
for i in range(-1, -(len(str1) + 1), -1):
    # output = output + str1[i]
    output += str1[i]

print(output)

print("//////")
output1 = ''
for i in str1:
    output1 = i+output1

print(output1)

# for i in range(len(str1)-1,-1,-1):
#     print(str1[i])

