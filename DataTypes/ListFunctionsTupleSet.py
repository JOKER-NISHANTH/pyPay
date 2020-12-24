# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:18:36 2020

@author: Nishanth
"""

'''
List Comprehension
'''

square = []
for i in range(1,10):
    square.append(i**2)
print(square)


print(" List Comprehension ")
x = [ i**2 for i in range(1,10)]
print(x)


print([ i**2 for i in range(1,10)])




print('Find Duplicate via count function')
fruits = ['orange','pear','banana','kiwi','apple','banana']
print(fruits)
print(fruits.count('apple'))

if fruits.count('apple') > 1:
    print('Apple is duplicate')
else:
    print("Nope")






print('Find Duplicate via count function')
fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print(fruits)
print(fruits.count('apple'))

if fruits.count('apple') > 1:
    print('Apple is duplicate')
else:
    print("Nope")





print("Remove first Duplicate element")
fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print(fruits)

if fruits.count('apple') > 1:
    fruits.remove('apple')
else:
    print('No Duplicate found')
print(fruits)





print('Remove last duplicate element')
fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print(fruits)
fruits.reverse()
if fruits.count('apple') > 1:
    fruits.remove('apple')

fruits.reverse()
print(fruits)






print("Learn index")
fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print(fruits)

i = fruits.index('apple')
print(f'First index of the apple is {i}')

i = fruits.index('apple',2)
print(f'Next index of the apple is {i}')





print('Learn Insert')
# Insert value is denote the index value
game = ['football','volleyball','handball']
print(game)
game.insert(2,'soccer')
print(game)





















