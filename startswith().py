s="python"
res=s.startswith("P")
print(res)
res=s.startswith("p",1,4)
print(res)
res=s.startswith("p",0,4)
print(res)
res=s.startswith("m")
print(res)
res=s.startswith("p")
print(res)
res=s.startswith("p",0)#only start index
print(res)
res=s.startswith("p",1)#only start index
print(res)
'''
Output:
False
False
True
False
True
True
False
'''
