'''Q . Write a program that takes a positive integer from the user and counts how many digits it 
has using a while loop. Do not convert the number to a string. 
Example: Input: 12345, Output: 5 '''

n = int(input('Enter a Number : '))
count = 0

if n == 0:
    count = 1 
else :
    while n > 0 :
        n = n //10
        count = count + 1

print(count)
