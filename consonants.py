s=input("Enter a word:")
print("Consonants in the word are:")
for char in s:
    if char not in 'aeiouAEIOU':
        print(char,end=" ")
'''
Output:
Enter a word:Aditya
Consonants in the word are:
d t y
'''
