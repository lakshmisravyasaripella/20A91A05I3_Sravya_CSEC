s=input("Enter string")
for char in s:
    if char.isalnum():
        print("True")
        break
else:
    print("False")
for char in s:
    if char.isalpha():
        print("True")
        break
else:
    print("False")
for char in s:    
    if char.isdigit():
        print("True")
        break
else:
    print("False")
for char in s:    
    if char.islower():
        print("True")
        break
else:
    print("False")
for char in s:    
    if char.isupper():
        print("True")
        break
else:
    print("False")
'''
Output:
Enter stringqA2
True
True
True
True
True
'''

