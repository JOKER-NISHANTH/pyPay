# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:47:18 2020

@author: Nishanth

what is meant by end here ? Default end is \n

"""


'''


why I decided to go with while ?
        Repeating action





We know that :
print
        11111
        22222
        33333
        44444
        55555


print(1)
print(1)    count = 0
print(1)    while count < 5:
print(1)        print(1,end="")
print(1)        count+=1


print(2)
print(2)    count = 0
print(2)    while count < 5:
print(2)        print(2,end="")
print(2)        count+=1

print(3)
print(3)    count = 0
print(3)    while count < 5:
print(3)        print(3,end="")
print(3)        count+=1

print(4)
print(4)    count = 0
print(4)    while count < 5:
print(4)        print(4,end="")
print(4)        count+=1

print(5)
print(5)    count = 0
print(5)    while count < 5:
print(5)        print(5,end="")
print(5)        count+=1


Using nested while loop



'''

count=0
while count < 5:
    print(1)
    count += 1



outer_loop = 0
while outer_loop < 5:
    inner_loop=0
    while inner_loop < 5:
        print(1,end="")
        inner_loop+=1
    print()
    outer_loop+=1



outer_loop = 0
while outer_loop < 5:
    inner_loop = 0
    while (inner_loop < 5):
        print(inner_loop,end="")
        inner_loop+=1
    print()    
    outer_loop+=1


outer_loop = 1
while outer_loop <= 5:
    inner_loop = 1
    while (inner_loop <= 5):
        print(inner_loop,end="")
        inner_loop+=1
    print()    
    outer_loop+=1


outer_loop = 0
while outer_loop < 5:
    inner_loop = 0
    while (inner_loop < 5):
        print(outer_loop,end="")
        inner_loop+=1
    print()    
    outer_loop+=1

outer_loop = 1
while outer_loop <= 5:
    inner_loop = 1
    while (inner_loop <= 5):
        print(outer_loop,end="")
        inner_loop+=1
    print()    
    outer_loop+=1




'''
1)      5 row         --> vertical      --> left to right
2)      5 column      --> herizontal    --> top to bottom



1       outer_loop = 1
2       while outer_loop <= 5:
3            inner_loop = 1
4            while (inner_loop <= 5):
5                print(outer_loop,end="")
6                inner_loop+=1
7            print()    
8            outer_loop+=1

============================================================

1)      5 row         --> which line decide the row         2
2)      5 column      --> which line decide the column      4


inner loop is responsible for deciding no.of.columns
outer loop is responsible for deciding no.of.row
    


        columns

row   1r,1c      1r,2c      1r,3c      1r,4c      1r,5c      
      2r,1c      2r,2c      2r,3c      2r,4c      2r,5c      
      3r,1c      3r,2c      3r,3c      3r,4c      3r,5c      
      4r,1c      4r,2c      4r,3c      4r,4c      4r,5c      
      5r,1c      5r,2c      5r,3c      5r,4c      5r,5c      


'''




row = 1
while row<= 3:
    
    column = 1
    while (column <= 5):
        print(row,end="")
        column+=1
    
    print()    
    row+=1


row = 1
while row<= 3:
    
    column = 1
    while (column <= 5):
    # while (column <= 5): --> in each row, there should be 5 columns
        print(row,end="")
        column+=1
    
    print()    
    row+=1




row = 1
while row <= 3:
    
    column = 1
    while (column <= row):
    # while (column <= row):  --> in each row , there should be row no of columns
        print(row,end="")
        column+=1
    
    print()    
    row+=1



row = 1
while row <= 5:
    
    column = 1
    while (column <= row):
        print(row,end="")
        column+=1
    
    print()    
    row+=1



row = 1
while row <= 5:
    
    column = 1
    while (column <= row):
        print(column,end="")
        column+=1
    
    print()    
    row+=1


row = 1
value=65
while row <= 5:
    
    column = 1
    while (column <= row):
        print(value,end="")
        value+=1
        column+=1
    
    print()    
    row+=1


'''
 
 chr --> character --> ASCII
 
 A,B,C,..,Z
 A -> 65 to 90
 
 a,b,c,..,z
 a -> 97 to 122   

 ord --> 

'''
row = 1
value=65
while row <= 5:
    
    column = 1
    while (column <= row):
        print(chr(value),end="")
        value+=1
        column+=1
    
    print()    
    row+=1


row = 1
value= 1
while row <= 5:
    
    column = 1
    while (column <= row):
        print(value,end="")
        value+=1
        column+=1
    
    print()    
    row+=1


row = 1
value= 65
while row <= 5:
    
    column = 65
    while (column <= value):
        print(chr(column),end="")
        column+=1
        
    
    print()    
    value+=1
    row+=1



