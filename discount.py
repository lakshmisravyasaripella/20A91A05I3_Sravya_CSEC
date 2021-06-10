amount=int(input("Enter amount"))
if 1000<amount<2000:
    discount=amount*(10/100)
    print("Discount is",discount)
    print("Total amount is",amount-discount)
elif 2000<amount<3000:
    discount=amount*(20/100)
    print("Discount is",discount)
    print("Total amount is",amount-discount)
elif 3000<amount<5000:
    discount=amount*(30/100)
    print("Discount is",discount)
    print("Total amount is",amount-discount)
elif amount>5000:
    discount=amount*(40/100)
    print("Discount is",discount)
    print("Total amount is",amount-discount)
else:
    print("There is no discount")
    print("Total amount is",amount)
'''    
Output:
Enter amount3800
Discount is 1140.0
Total amount is 2660.0     
'''  
