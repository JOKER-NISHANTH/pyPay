# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:33:22 2020

@author: Nishanth
"""

'''

Immutability Property  -->  Not change

    whenever we change any value for a variable,the existing value
    present in a particular addresss will not get changed.

         Instead, it will point out to new memory address

        Here Memory can be waste , can't recallable

   ** Python is  Garbage Collection(unused memory) ** --> Multi-threading

'''

House_no = 10
print("Type : ",type(House_no))
print("Address : ",id(House_no))


print("After Change House ")
House_no = 12
print("Address : ",id(House_no))






mark = 90
print(f"Address { mark } and address { id(mark) }")
print(f"After rechecking { mark + 5 } and address { id(mark) }")



count = 0
print("Address : ",id(count))

count = 1
print("Address : ",id(count))

count = 2
print("Address : ",id(count))





captain = 'Nishanth'
print("Address : ",id(captain ))

captain = 'Nisha'
print("Address : ",id(captain ))





state1="tamil nadu"
state2="tamil nadu"
print("Address : ",id(state1))
print("Address : ",id(state2))


state1="tamilnadu"
state2="tamilnadu"
print("Address : ",id(state1))
print("Address : ",id(state2))



'''

Immutability is related with data_types or Identifiers

    Immutability ==> Changes in Memory Address
    Immutability ==> Not with values

'''


city1 = "maduari"
city2 = "maduari"

print(" is --> compares the memory address of the given identifiers ")
print(id(city1)  ,id(city2))
print(city1 is city2)

print(" == --> compares the value of the given identifiers")
print(id(city1)  ,id(city2))
print(city1 == city2)



print('''
      
      Immutable DataType
      
      float , integer , boolean ,string , byte , complex
      
      ''')



