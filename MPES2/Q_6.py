'''Q6. Find Maximum in a List 
Given the list values = [34, 12, 89, 23, 67, 45, 90, 56], write a program to find the maximum 
value using a for loop. Do not use the built-in max() function. 
Expected Output: 90 '''

n = input ("Enter list of numbers :")
L1 =[int(x) for x in n.split(",")]
big_one = 0
i = 0

for i in range (len(L1)) :
    if big_one < L1[i] :
        big_one = L1[i]
    i = i + 1

print (big_one)
