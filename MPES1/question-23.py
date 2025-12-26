salary = int(input('Enter amount of salary :'))
experience = int(input('Enter total yaers of experience :'))
if salary >= 40000 and experience >= 2:
    if experience < 5:
        bonus = salary * 0.1
        print('junior bonus :',bonus)
    else :
        bonus = salary * 1.5
        print('senior bonus :',bonus)

else :
    print('no bonus applied')
