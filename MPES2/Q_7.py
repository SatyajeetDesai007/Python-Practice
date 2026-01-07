'''Q7. Sum of Dictionary Values 
Given the dictionary prices = {"apple": 50, "banana": 30, "orange": 40, "mango": 80}, write a 
program to calculate the total of all prices using a for loop. 
Expected Output: 200'''

d = {"apple": 50, "banana": 30, "orange": 40, "mango": 80}
sum = 0

for i in d.keys ():
    sum = sum + d[i]

print(sum)