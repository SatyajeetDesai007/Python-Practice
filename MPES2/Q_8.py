'''Q. Write a program that takes a number N from the user and prints a pattern of stars. The first 
line should have 1 star, second line 2 stars, and so on until N stars.'''

n = int(input('Enter Number : '))
i = 1 

for i in range (n + 1):
    print(i * '*')
    i = i + 1

