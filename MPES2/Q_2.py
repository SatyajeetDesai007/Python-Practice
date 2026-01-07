'''
Q2. Count Vowels in a String 
Write a program that takes a string from the user and counts how many vowels (a, e, i, o, u - both uppercase and lowercase) are present in it. Use a for loop to iterate through each 
character. 
Example: Input: "Hello World", Output: 3 

'''

text = input ("Enter a String :")
vowels = "aeiouAEIOU"
count = 1

for char in text:
    if char in vowels:
        count += 1
print(count)