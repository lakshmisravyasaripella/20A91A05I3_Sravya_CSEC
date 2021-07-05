list1=["AEC","ACET","SLS"]
print(list1)
list2=["A9","P3","G5"]
print(list2)
#Add list2 values to the end of list1
list1.extend(list2)
print("After extending")
print(list1)
print(list2)
list2.extend([22,256,789])
print(list2)
list1.extend(list2,[22,56,77])
print(list1)
'''
Output:
['AEC', 'ACET', 'SLS']
['A9', 'P3', 'G5']
After extending
['AEC', 'ACET', 'SLS', 'A9', 'P3', 'G5']
['A9', 'P3', 'G5']
['A9', 'P3', 'G5', 22, 256, 789]
TypeError: list.extend() takes exactly one argument (2 given)
'''
