'''Q. Write a program that takes N from the user and prints a right-angled triangle pattern using 
numbers. '''

n =  int ( input('enter a number :'))
s = []

for i in range ( 1 , n+1):
    for j in range (1 , n+1):
        if i >= j : 
            s.append(j)
            j += 1
    print(s)
    s.clear()
    i += 1