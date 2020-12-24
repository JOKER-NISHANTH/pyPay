# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:34:47 2020

@author: Nishanth

_variable       --> Protected

__variable      --> Private

__variable__    --> Magic variables


Keywords --> 34

"""

print("Arithmetic Operators")
print("Bodmas : ",(500-5*10)+50)
print("Div : ",80/4)
print("Floor Div : ",80//4)
print("Mul : ",2*3)
print("Power : ",2**3)
print("Mod : ",10%3)

print("-"*10)
# Identifier or reference_variable or variable  = value
width = 100
height = 5 * 9
print(width * height)

print("-"*10)
tamil,english,maths,computer_science = 80,85,99,100
print(tamil+english+maths+computer_science )

print("-"*10)
print("Calculate Tax from Salary")
Salary=500000
tax = Salary * (10/100)

print(tax)
print(int(tax))

print("-"*10)


print("Learn Underscore Operator Usage")
print(" Underscore return previous value")
Hack = 50
print(Hack)
print( 50 + _ )


print("-"*10)

print("Learn Round of Functuon")
# round(value,decimal_digit_value you went)
price = 121.99
tax = 4.5
print(price*tax)
print(round(price*tax,2))

print("-"*10)






