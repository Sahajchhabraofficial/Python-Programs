#Create dictionary and add five key-value pairs using user input.
dit={}
for i in range(5):
    key=input("Enter key:")
    value=input("Enter value:")
    dit.update({key: value})
print(dit)