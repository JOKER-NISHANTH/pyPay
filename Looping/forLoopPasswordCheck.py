# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:30:48 2020

@author: Nishanth
"""


'''
characters  - count
numbers     - count

1) User - input string


'''

# nishanthmohan2000@gmail.com

word = input(" Enter your word : ")
i = 0
while i < len(word) :
    print(word[i])
    i +=1


word = input(" Enter your word : ")    
length = len(word)
for letter in range(length):
    print(word[letter])
    
    
    
'''

Here A and Z is place ASCII value present  A = 65 and Z = 90

'''    
print("\n Printing Capital letter on word ")    
word = input(" Enter your word : ")    
length = len(word)
for letter in range(length):
    if (word[letter] >= "A" and word[letter] <= "Z"):
        print(word[letter])
    
    
    
'''

Here a and z is place ASCII value present   a = 97 and z = 122

'''    
    
print("\n Printing Small letter on word ")    
word = input(" Enter your word : ")    
length = len(word)
for letter in range(length):
    if (word[letter] >= "a" and word[letter] <= "z"):
        print(word[letter])
    


'''

Here 0 and 9 is place ASCII value present 0 = 48  and 9 = 57

'''


print(" Password Verification ")
countOfAlphabets = 0
countOfNumbers = 0
countOfSpecialCharacters = 0
word = input(" Enter your word : ")    
length = len(word)
if length < 8 :
    print("No, Please enter more characters ")
else:
    for letter in range(length):
        if ((word[letter] >= "a" and word[letter] <= "z") or (word[letter] >= "A" and word[letter] <= "Z")):
            countOfAlphabets += 1
        elif(word[letter] >= '0' and word[letter] <='9'):
            countOfNumbers += 1
        else:
            countOfSpecialCharacters += 1

    print(f"{countOfAlphabets} Alphabets are present ")
    print(f"{countOfNumbers} Numbers are present ")
    print(f"{countOfSpecialCharacters } SpecialCharacters are presernt")
    



print(" Password Verification using Built-in-function ")
countOfAlphabets = 0
countOfNumbers = 0
countOfSpecialCharacters = 0
word = input(" Enter your word : ")    
length = len(word)
if length < 8 :
    print("No, Please enter more characters ")
else:
    for letter in range(length):
        if (word[letter].isalpha()) :
            countOfAlphabets += 1
        elif(word[letter].isdigit()) :
            countOfNumbers += 1
        else:
            countOfSpecialCharacters += 1
    
    print(f"{countOfAlphabets} Alphabets are present ")
    print(f"{countOfNumbers} Numbers are present ")
    print(f"{countOfSpecialCharacters } SpecialCharacters are presernt")




'''
Task

    Check mobile
    Check email ID

'''



'''

nishanth        n
nishant         ni
nishan          nis
nisha           nish
nish            nisha
nis             nishan
ni              nishant
n               nishanth


     row = 8
     column = 8
'''

row = 1
while row <= 8:
    column = 1
    while column <= row:
        print(row,end="")
        column +=1
    
    print() 
    row +=1
    
        
    
        
word = 'nishanth'
for letter in range(len(word)):
    print(word[letter],end=" ")
print()
for letter in range(len(word)-1):
    print(word[letter],end=" ")
print()
for letter in range(len(word)-1-1):
    print(word[letter],end=" ")
print()
for letter in range(len(word)-1-1-1):
    print(word[letter],end=" ")
print()
for letter in range(len(word)-1-1-1-1):
    print(word[letter],end=" ")
    
    
    
    

word = 'nishanth'    
count = len(word)
for letter in range(count):
    print(word[letter],end=" ")
print()
count -= 1
for letter in range(count):
    print(word[letter],end=" ")
print()
count -= 1
for letter in range(count):
    print(word[letter],end=" ")
print()
count -= 1
for letter in range(count):
    print(word[letter],end=" ")
print()
count -= 1
    
    


word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(word[letter],end=" ")
    print()
    count +=1






word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(word[letter],end=" ")
    print()
    count -=1



word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(word[letter],end=" ")
    print()
    count +=1



    