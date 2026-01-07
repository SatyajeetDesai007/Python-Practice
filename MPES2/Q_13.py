'''Q .Given list1 = [1, 2, 3] and list2 = ['a', 'b', 'c'], write a program to print all possible pairs where 
the first element comes from list1 and the second from list2. '''


L1 = [1,2,3]
L2 = ['a','b','c']

for i in L1 :
    for j in L2 :
        print((i,j),end=',')
    