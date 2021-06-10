n=int(input("Enter number"))
d=int(input("Enter the number of digits"))
rev=0
for i in range(0,d):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("The reverse of the given number is",rev)
'''
Output:
Enter number79898649
Enter the number of digits8
The reverse of the given number is 94689897
'''
