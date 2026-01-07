'''Q. Write a program that takes N from the user and prints an inverted triangle pattern.'''

n = int (input('enter a number :'))
i = n
s = []
for i in range (n , 0,-1):
    for i in range (i ,0,-1):
        s.append(i)
    print(s)
    s.clear()
