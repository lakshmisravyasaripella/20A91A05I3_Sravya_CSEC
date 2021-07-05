list1=[234,1,2,3,-1,768]
list2=[365,678,-1,2,456]
list1.extend(list2)
list3=list1.copy()
list3.sort()
print(list3)
'''
Output:
[-1, -1, 1, 2, 2, 3, 234, 365, 456, 678, 768]
'''
