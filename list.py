mylist = ["apple", "banana", "cherry", "apple"]

print(mylist)
print(mylist[0])
print(mylist[1])


print(len(mylist))
print(mylist[2:4])

if "apple" in mylist:
    print("apple exists")

mylist.insert(2, "grapes")
mylist.append("hello")

print(mylist)

for x in mylist:
    print(x)

print("=================")

for x in range(len(mylist)):
    print(mylist[x])
