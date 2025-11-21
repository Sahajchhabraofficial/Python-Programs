#Write a python program to find the largest element in a list and then reverse the
#list contents and display it. Don’t use in-built functions for the program.
lst=[12,35,78,62,54,89]
Largest=lst[0]
for i in range(len(lst)):
    if lst[i]>Largest:
        Largest=lst[i]
print("Largest element in the list is:",Largest)
print("Reversed list : ",lst[::-1])