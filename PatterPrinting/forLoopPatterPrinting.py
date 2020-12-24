# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:20:28 2020

@author: Nishanth
"""


word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(letter,end=" ")
    print()
    count +=1




word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(chr(letter+65),end=" ")
    print()
    count +=1




word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(chr(letter+97),end=" ")
    print()
    count +=1





word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(chr(terms+65),end=" ")
    print()
    count +=1



word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(chr(terms+97),end=" ")
    print()
    count +=1





word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print(terms,end=" ")
    print()
    count +=1



word = 'nishanth'    
count = len(word)
count = 1
for terms in range(len(word)):
    for letter in range(count):
        print("*",end=" ")
    print()
    count +=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print("*",end=" ")
    print()
    count -=1


'''
Given Task

        * * * * * * * * #
        * * * * * * * # #
        * * * * * * # # #
        * * * * * # # # #
        * * * * # # # # #
        * * * # # # # # #
        * * # # # # # # #
        * # # # # # # # #

'''



word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print("*",end=" ")
    print('#')
    count -=1



word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print("*",end=" ")
    print("#",end=" ")
    print()
    count -=1

word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(terms):
        print(" ",end=" ")
    print("#",end=" ")
    print()
    count -=1


'''
terms = 7
for Hash in range(terms +1 ):
    print("#")
'''


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(terms):
        print(" ",end=" ")
    print("#",end=" ")
    print()
    count -=1



for terms in range(len(word)):
    print(terms)


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print("#",end=" ")
    print()
    count -=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print("*",end=" ")
    print()
    count -=1

word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print(" * ",end=" ")
    print()
    count -=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print(Hash+65,end=" ")
    print()
    count -=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print(chr(Hash+65),end=" ")
    print()
    count -=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print(letter+65,end=" ")
    print()
    count -=1



word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print(chr(letter+65),end=" ")
    print()
    count -=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print(terms+65,end=" ")
    print()
    count -=1


word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print(" ",end=" ")
    for Hash in range(terms +1 ):
        print( chr(terms+65) ,end=" ")
    print()
    count -=1









word = 'nishanth'    
count = len(word)
for terms in range(len(word)):
    for letter in range(count):
        print("*",end=" ")
    for Hash in range(terms +1 ):
        print("#",end=" ")
    print()
    count -=1

