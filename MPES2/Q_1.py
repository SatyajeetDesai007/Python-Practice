'''
Write a program that takes a positive integer N from the user and calculates the sum of all 
natural numbers from 1 to N using a for loop. Display the result. 
Example: If N = 5, output should be 15 (1+2+3+4+5) 
'''

n = int(input("Enter a Number : "))
i = 1 
sum = 0

for i in range (n+1) : 
    sum = sum + i
    i = i + 1

print(sum)