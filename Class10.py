# printing of prime numbers between 1 to 50
for i in range(2, 51):
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime == True:
        print(i, end=" ")

l1 = ["chandra", "krishna", "nandu", "vivek", "vani", "rajitha", "sandeep"]

print("///////break///////////")
for i in l1:
    if i == "nandu":
        print(i)
        break

# break,continue
# break => it will stop/break the iteration
# continue => it will skip the current iteration and proceed further loop
print("/////Continue////////////")
for i in l1:
    if i == "chandra":
        print("printing from inside if before continue")
        continue
        print("after continue")

    print(i)
print("////////")
for i in range(6):
    if i == 1 or i == 4:
        continue

    print(i)

# pass => is used to skip the execution of code which is not implemented/if something not implemented we can skip the
# execution
for i in range(3):
    pass
if x == 5:
    pass

