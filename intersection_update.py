set1={33,56,77,33,21,12}
set2={12,54,77,35,33,56,99}
set3=set1.intersection_update(set2)
print(set3)
print(set1)
print(set2)
'''
Output:
None
{56, 33, 12, 77}
{33, 99, 35, 54, 56, 12, 77}
'''
