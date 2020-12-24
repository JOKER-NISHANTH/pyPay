# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:39:14 2020

@author: Nishanth
"""

'''
Compound DataTypes

'''

Squares = [1,4,9,16,25]
print(Squares[0])
print(Squares[-3:])
print(Squares[:-3])
print(Squares[:])




A = Squares + [50,99,77,22]
print(A)


A[1] = 33
print(A)

Squares.append(44)
print(Squares)


Squares.append(2**3)
print(Squares)

Squares.append([11,10])
print(Squares)



Letters = ['A','B','C','D','E']
print(Letters)

print(Letters[2:5])




Letters[2:5] = ['z','y','x']
print(Letters)



Letters[2:5] = []
print(Letters)



Letters[:] = []
print(Letters)





Letter = ['i','j','k','l','m','n']
print(len(Letter))



alpha = ['a','b','c']
numbers = [1,2,3]
both = [alpha , numbers]
print(both,' ',type(both))
print(alpha[0],' ',type(alpha[0]))
print(numbers[0],' ',type(numbers[0]))

print(len(both))
print(both[0])
print(both[1])
print(both[0][1])


for LIST in alpha:
    print(LIST,end=' ')


for LIST in numbers:
    print(LIST,end=' ')



both=str(both)

for inner_list in both:
    for list_item in inner_list:
        print(list_item,end=" ")


print("Alphabhate")

# if type(items) == str and itmes.isalpha():
for inner_list in both:
    for list_item in inner_list:
        if list_item.isalpha():
            print(list_item,end=" ")


print("Print Digit's only")
# # if type(items) == int and itmes.isdigit():
for inner_list in both:
    for list_item in inner_list:
        if list_item.isdigit():
            print(list_item,end=" ")



Vo = ['a','b','c','e','i']
for item in Vo:
    if (item == 'a' or item == 'e' or item == 'i' or item == 'o' or item == 'e'):
        print(item,end=' ')











