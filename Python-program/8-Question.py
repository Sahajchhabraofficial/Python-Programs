#follow the commands:
sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#Get the first 3 elements in reverse order.
print("First three elements in reverse:",sample_list[2::-1])
#Exclude the first and last elements, then return every second element fromthe result.
print("Excluding first and last elements:",sample_list[1:-1:2])
#Reverse the list and return every third element.
print("Reversed list with every third element:",sample_list[::-3])
#Get the 4th, 3rd, and 2nd last elements in the same order.
print("4th, 3rd and 2nd last elements:",[sample_list[-4],sample_list[-3],sample_list[-2]])
#Get [90, 70, 50, 30] using slicing only.
print("Elements [90, 70, 50, 30]:",sample_list[-2:2:-2])