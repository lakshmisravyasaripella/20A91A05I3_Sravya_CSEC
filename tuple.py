t=(10,23,45,457,45,67,89)
res1=t.count(45)
print(res1)
res2=t.index(457)
print(res2)
res3=t.index(456)
print(res3)
'''
Output:
2
3
ValueError: tuple.index(x): x not in tuple
'''
