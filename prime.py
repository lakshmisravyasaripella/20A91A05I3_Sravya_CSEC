n=int(input("Enter any number"))
i=1
flag=0
while i<=n:
    if n%i==0:
        flag=flag+1
    i=i+1
if flag==2:
    print("It is a prime number")
else:
    print("It is not a prime number")
#Output:
Enter any number91
It is not a prime number

Enter any number29
It is a prime number
    
        
