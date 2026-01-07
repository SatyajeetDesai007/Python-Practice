'''
Q3. Multiplication Table 
Write a program that takes a number from the user and displays its multiplication table from 
1 to 10. Each line should show the complete multiplication expression. 
Example: For input 7: "7 x 1 = 7", "7 x 2 = 14", ... "7 x 10 = 70"
'''

number = int(input("Enter a Number : "))
i = 1
while (i <= 10):
    multiplication = i * number
    print(number, " * ", i ," = ",multiplication)
    i = i + 1
