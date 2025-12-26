a = 9
b = 4
c = 6
complex_condition = a > b and b > c or b < c or not(a == c) and (a+b)%c == 1
print('complex condition is : ', complex_condition)

if complex_condition :
    final_result = a * b - c
    print('Path A - Result :', final_result)
else :
    final_result : a + b + c
    print('path B - Result : ',final_result)

print('Data Type :', type(final_result).__name__)    
                        
                        
