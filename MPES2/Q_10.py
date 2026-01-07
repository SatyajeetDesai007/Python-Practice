'''Q. Given the list data = [3, 8, 15, 22, 7, 36, 41, 50, 19, 64], write a program to create a new list 
containing only the even numbers using a for loop. 
Expected Output: [8, 22, 36, 50, 64]'''

data = [3, 8, 15, 22, 7, 36, 41, 50, 19, 64]
op = []

for i in data :
    if i % 2 == 0 :
        op.append(i)

print(op)