#Write a program in python, which accepts a list of numbers and a numeric value
#by which all elements of the list are shifted to left.
lst=[]
count=0
for i in range(5):
    element=int(input("enter element of list: "))
    lst.append(element)
num=int(input("enter a numeric value: "))
for k in range(num,len(lst)):
    print(lst[k],end="",sep=",")
    count+=1
for y in range(0,num):
    print(lst[y],end="")