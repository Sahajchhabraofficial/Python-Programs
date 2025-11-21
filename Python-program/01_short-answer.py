#What will be the output of the following python program?
data = [10,20,30, 60,70]
data[3:3]=[40,50]
print(data)
data.pop(3)
print(data)
data.extend([10,20])
print(len(data))