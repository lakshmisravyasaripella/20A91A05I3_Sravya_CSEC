s=input("Enter a word:")
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print("Vowel exists")
        break
else:
    print("Does not contain vowels")
'''
Output:
Enter a word:python
Vowel exists
Enter a word:scn
Does not contain vowels
Enter a word:Aditya
Vowel exists
'''
   
