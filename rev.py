n=int(input("Enter number"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("The reverse of the given number is",rev)
#Output:
Enter number534879
The reverse of the given number is 978435
