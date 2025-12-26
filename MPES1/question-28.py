test1 = 88
test2 = 76
test3 = 92
avg = (test1 + test2 + test3) / 3
average = round(avg,2)
print('Average score :', average)
if average >= 85 :
    grade = 'A'
elif average >= 75 :
    grade = 'B'
elif average >= 65 :
    grade = 'C'
else :
    grade = 'F'
print('Final grade : ', grade )
result = "PASS" if grade != 'F' else "FAIL"
print("Result : ",  result )
