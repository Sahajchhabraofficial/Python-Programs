#what will bet the ansswer of the given list.
data = [10,20,30]
data[1:3]=[5,10]
print(data)
data.extend([3,4])
x =data.count(10)
print(data[x:])
data.sort()
print(data)
print(data.pop(2))