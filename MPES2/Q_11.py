'''Q. Write a program to display a 5×5 multiplication table grid. The entry at row i and column j 
should be i × j. Format the output neatly with proper spacing. '''

n = int(input('Enter A number : '))
s = []

for i in range (1 , n + 1):
    for j in range (1 , n+1):
        a = i * j 
        s.append(a)
        j += 1
    print(s)
    s.clear()
    i += 1