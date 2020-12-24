# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:09:51 2020

@author: Nishanth
"""


print("=="*5," Learn TypeCasting ","=="*5)



First = 57
Second=98.21
total = First + Second
print(type(total), " ", total)

average = total/2
print(type(average), " ", average)

print("=="*5," Change to int ","=="*5)

average=int(average)
print(type(average), " ", average)



shirt_price=500
pants_price=650
total = shirt_price + pants_price
print(total)

print("Here comma is used to sep  and pass two args in print function ")
print("1st args<string> ,2nd args<data_type>")
print("your Bill is ",total)
print("your Bill is "+str(total))

#print("your Bill is "+total) 
#TypeError: can only concatenate str (not "int") to str





print("=="*5," bool to int ","=="*5)

print("In bool data_type 0 is False , others True ")

a=1
print(bool(a))
b=0
print(bool(b))
c=1234
print(bool(c))
d=1.5
print(bool(d))
e=0.0
print(bool(e))
f=0.1
print(bool(f))


name = 'abcd'
print(bool(name))

name = ''
print(bool(name))

name = ' '
print(bool(name))



print("=="*5," int to complex ","=="*5)
value = 50
print(complex(value)) # what is complie ?


print(complex(7,9)) 

print(complex('7',9)) 
# TypeError: complex() can't take second arg if first is a string

print(help(complex()))

# |  __add__(self, value, /)
# |      Return self+value.

Value=34.65
print(complex(Value,5))

print(complex(True,True))
print(complex(True,False))


a = "5A"
#print(complex(a)) 
# ValueError: complex() arg is a malformed string

print("String is take real part ")
print(complex("5"))

