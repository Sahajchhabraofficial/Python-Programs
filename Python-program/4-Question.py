#Write a program to create a list of elements L and then create another list named
#‘indexList’ that stores the indices of all Non-Zero Elements of L.
Lst=[34,52,32,91,24,24]
IndexList=[]
for i in range(len(Lst)):
    if Lst[i]!=0:
        IndexList.append(i)
print("List of elements in Lst: ",IndexList)