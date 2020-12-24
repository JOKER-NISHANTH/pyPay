# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:46:59 2020

@author: Nishanth
"""

print("=="*5,"Learn Int Data-Type","=="*5)

no = 123
print(no)
print("Learn Type Function")
print(type(no))
print(" id Function ")
print(id(no)) # return object address

'''
    # Real-life values are in base 10

    # Base 2 ---> Binary 0,1

    # Base 8 ---> Oct 0,1,..,7

    # Decimal No --> 0,1,..,9

    # Base 16 ---> Hex 0,1,..,9,A,B,C,D,E,F [or] 0,1,..,9,a,b,c,d,e,f

'''


'''

    0b(or)B1111 --> here 1*(2**3)+1*(2**2)+1*(2**1)+1*(2**0) = 8 + 4 + 2 +1 = 15

'''

print("Learn Decimal Conversion ")

print("Binary to Decimal")
value = 0b1111 
print(value)

Value= 0B1010
print(Value)
print("=="*10)

print("Octal to Decimal")
Oct = 0o1111
print(Oct)
print("=="*10)

print("HexaDecicmal to Decimal")
Hex = 0x123
print(Hex)
HEX = 0xABC
print(HEX)
HEx = 0xabc
print(HEx)
print("=="*10)


print("Leanr Decimal to bin ,Oct ,hex Converstion ")
print("Decimal to Binary")
print(bin(10))
print("Decimal to Oct")
print(oct(10))
print("Decimal to Hex")
print(hex(10))
print("=="*10)

print("Hex to Bin")
print(bin(0xBEEF))


print("=="*5,"Learn Float Data-Type","=="*5)
'''
    Real-Life 
        eg:
            pi=3.14

    no = 1.234

    Float values Default in Decimal only not in oct,hex and bin

    no = ox123.22
        return Synatx error

    Support Exponacitional or scientific notation
    no = 5.6e3
    
        e3 is 10 power 3 = 1000
'''

print(1.234)
print(5.6e3)

print(type(1.234))
print(id(1.234))

print("=="*5,"Learn Complex Data-Type","=="*5)

''' a+bj ==> a is real b is imaginary
    real part allowed ==> bin,oct,hex,dec
    imag part allowed only dec value '''

Com=5+6j
print(Com)
print(Com.real)
print(Com.imag)

print("=="*5,"Learn Boolean or bool Data-Type","=="*5)
''' bool --> True [1] and False [0] '''
mark1=98
mark2=96

print(mark1>mark2)
print(mark1<mark2)
print(mark1==mark2)
print(mark1>=mark2)
print(mark1<=mark2)
print(True+False)
print(False+False)
print(True+True)
print(False+True)


print("=="*5,"Learn String Data-Type","=="*5)
print("\n\tDouble Quote")
name ="Nishanth"
print(name)
print("\n\tSingle Quote")
Name = "Cyber_Nisahnth"
print(Name)
print("\n\tTriple Quote")
NAME="""
        I am Nisahnth
        Form Sathy
        I Did my Schooling at Gobi
        """
print(NAME)


print("=="*5,"Learn BackSlach usage ","=="*5)
for i in \
range(1,10,2):
    print(i)
    