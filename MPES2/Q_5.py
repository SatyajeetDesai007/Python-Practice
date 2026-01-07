'''
Q5. Factorial Using While Loop 
Write a program that takes a non-negative integer from the user and calculates its factorial 
using a while loop. Remember: 0! = 1 and n! = n × (n-1) × (n-2) × ... × 1 
Example: Input: 5, Output: 120 
'''

n = int(input("Enter a number : "))
factorial = 1
i = 1

while i <=n :
    factorial = i * factorial
    i = i + 1

print(factorial)