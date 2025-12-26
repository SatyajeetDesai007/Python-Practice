side1 = 5
side2 = 6
side3 = 0
if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1 :
# in above condition we use property of traingle = sum of any two sides of triangles is greater than remaining side.
    perimeter = side1+side2+side3
    print('valid traingle with perimeter : ', perimeter)
else :
    print('invalid triangle')
