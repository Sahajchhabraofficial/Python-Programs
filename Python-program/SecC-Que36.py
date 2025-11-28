#Create a list of first 20 even numbers using loop
Even=[]
for i in range(1,21):
    if i%2==0:
        Even.append(i)
print(Even)