#Program to check if an element exists in a list.
combo=0
Lst=[10,20,30,40,50]
search=int(input("enter a element: "))
for i in range(5):
    if search==Lst[i]:
        combo=5
if combo==5:
    print("Exists")
else:
    print("Not Exists")