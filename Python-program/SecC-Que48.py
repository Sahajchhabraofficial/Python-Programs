#Take 5 names from user, store in list, sort alphabetically.\
names=[]
for i in range(5):
    name=input("Enter name:")
    names.append(name)
names.sort()
print("Sorted names:", names)