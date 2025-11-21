#Write the most appropriate list method to perform the following task in a givenlist my_list:
"""(a) Add element at 4th position in the given list
(b) Add element in the last position of the list
(c) Delete 2nd element from the given list
(d) Delete the given element from the given list
(e) Add elements (more than one at the end of the given list)"""
my_list = [1, 2, 3, 4, 5]
#(a)
my_list.insert(3, 'a') 
#(b)
my_list.append('b')  
#(c)
my_list.pop(1)  
#(d)
my_list.remove(3)  
#(e)
my_list.extend([6, 7, 8])  
print(my_list)
