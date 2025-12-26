flag1 = True
flag2 = False
flag3 = True
condition1 = flag1 and flag2 or flag3
condition2 = flag1 and (flag2 or flag3)
print(condition1)
print(condition2)
print(condition1 == condition2)
