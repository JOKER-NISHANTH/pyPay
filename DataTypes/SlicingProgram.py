# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:11:49 2020

@author: Nishanth
"""

print("=="*5,"String Slicing ","=="*5)

name = 'nishanth'
print(name[0].upper())

name= 'cyber_nishanth'
print(name[0].upper() + name[1:-2] + name[-1].upper())






print("=="*5," len(object) ","=="*5)
name= 'cyber_pearl'
print("Return the string length",len(name))      
      
print(name[0].upper() + name[1:len(name)-1] + name[-1].upper())

print(name[:len(name)-1] + name[-1].upper())



print("In slicing stop and step value is not give in -ive value ,\n return null string becoz backward slicing is not possiable uning -ive value")



print(name[2:len(name)-1:-1])
print(name[2:len(name)-2:-1])
print(name[2::-1])
print(name[2::1])
print(name[2::2])







Name= " Black" + "Pearl"
print(Name)


HeartBeat = " lub dub " * 72
print(HeartBeat)



print("=="*5," Learn in Operator ","=="*5)

#In english ==> Check if 'a' is present in 'nishanth'

myName= "nishanth"
print('a' in myName)
print('A' in myName)




































