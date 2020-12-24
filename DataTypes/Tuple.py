# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:27:10 2020

@author: Nishanth
"""

'''

Tuple is immutable
print(dir(tuple))

'''

num = (1,2,3)
print(num," ",type(num))

num = (1)
print(num," ",type(num))

t=()
print(t," ",type(t))

num = (1,)
print(num," ",type(num))


num[0] = 2
#print(num) # TypeError: 'tuple' object does not support item assignment


n = (1,2,3,4,5,6,7,8,9)
item = 0
while item < len(n):
    print(n[item],end='')
    item+=1


for i in n:
    print(i,end='')


#n.remove(8) # AttributeError: 'tuple' object has no attribute 'remove'
#n.append(8) # AttributeError: 'tuple' object has no attribute 'append'





