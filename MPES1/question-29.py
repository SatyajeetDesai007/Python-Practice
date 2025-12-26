year = 1996
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('this is leap year......')
        else :
            print('this is not a leap year.....')
    else :
        print('this is leap year......')
else :
    print('this is not a leap year...')
