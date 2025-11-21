#Write a Python program that accepts a list L of numbers and finds the sum of all
#even numbers and the sum of all odd numbers.
L=[12,45,23,56,78,91,34,67]
even_nos=0
odd_nos=0
for i in range(len(L)):
    if L[i]%2==0:
        even_nos+=L[i]
    else:
        odd_nos+=L[i]
print("Sum of even numbers:",even_nos)
print("Sum of odd numbers:",odd_nos)