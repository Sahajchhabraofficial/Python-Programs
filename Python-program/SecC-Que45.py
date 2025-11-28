#From this list create list of even numbers.
L=[2,5,8,11,14]
Even=[]
for i in L:
    if i%2==0:
        Even.append(i)
print(Even)