n=int(input("Enter number"))
i=1
print("The factors of n are:")
while i<=n:
    if n%i==0:
        print(i,end=" ")
    i=i+1
'''    
Output:
Enter number18
The factors of n are:
1 2 3 6 9 18     
'''
