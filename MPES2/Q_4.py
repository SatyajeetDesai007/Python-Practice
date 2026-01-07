'''Q4. Reverse a List 
Given the list numbers = [10, 20, 30, 40, 50], write a program to create a new list containing 
the elements in reverse order using a for loop. Do not use the built-in reverse() method or 
slicing. 
Expected Output: [50, 40, 30, 20, 10] '''

L1 = input ("Enter numbers in list : ")
L2 = L1.split()
reversed_list = []
i = len(L2)

for i in range(len(L2)-1,-1,-1):
    reversed_list.append(L2[i])

print (reversed_list)

