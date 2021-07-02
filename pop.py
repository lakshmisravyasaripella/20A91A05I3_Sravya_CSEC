list=[155,176,231,222,155,231,220,150,176,125]
print(list)
remove_element=list.pop()#pop without index
print(remove_element)
print(list)
remove_element=list.pop(2)#pop with index
print(remove_element)
print(list)
'''
Output:
[155, 176, 231, 222, 155, 231, 220, 150, 176, 125]
125
[155, 176, 231, 222, 155, 231, 220, 150, 176]
231
[155, 176, 222, 155, 231, 220, 150, 176]
'''
