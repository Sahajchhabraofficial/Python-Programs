#write a program to count vowels in a string.
string="Interview"
for i in range(len(string)):
    if string[i] in 'aeiouAEIOU':
        print(string[i])