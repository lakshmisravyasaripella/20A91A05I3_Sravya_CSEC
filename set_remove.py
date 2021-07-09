s={10,20,30,40,70}
s.remove(40)
print(s)
s.remove(90)
print(s)
'''
Output:
{20, 70, 10, 30}
Traceback (most recent call last):
  File "C:/Users/Domain/Documents/set_remove.py", line 4, in <module>
    s.remove(90)
KeyError: 90
'''
