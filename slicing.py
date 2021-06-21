s="python"
print(s[0])
print(s[0:4])
print(s[0:13])
print(s[1:5:2])#[start:end:stepcount]
print(s[13])
'''
Output:
p
pyth
python
yh
Traceback (most recent call last):
  File "C:/Users/Domain/Documents/slicing.py", line 6, in <module>
    print(s[13])
IndexError: string index out of range
'''
