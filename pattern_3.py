n=int(input("Enter number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")        
#Output:
Enter number of rows5
1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 

1 2 3 4 5 

1 2 3 4 

1 2 3 

1 2 

1 
    