# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:14:36 2020

@author: Nishanth
"""

print("Mutable DataTypes in Python")
print(" Some Compound DataTypes comes under Mutable DataType")

name = "nisha"
print(name[0])
print(name[1])
print(name[2])
#name[0]="i" # TypeError: 'str' object does not support item assignment
print(name)



print("Convert Python to Jython")
program = "python"
y=program[1:]
print("J"+y)


'''

Mutable DataType
    1.List
    2.ByteArrays
    3.Set
    4.Dict

Compound DataType
    1.List
    2.Set
    3.Tuple
    4.Dict

'''

'''
--> mutable datatype
--> compound datatype
--> List are separated by comma
--> Accepts both homegeneous and heterogeneous
'''
print(" homegeneous ")
names = ['nisha','vasee','sandy','nandy']
print(type(names))


print(" heterogeneous ")
names = ['nisha','vasee','sandy','nandy',161,9.9,False]
print(type(names)," ",id(names))
print(names)
names[0]='nishanth'
print(names)
print(type(names)," ",id(names))





