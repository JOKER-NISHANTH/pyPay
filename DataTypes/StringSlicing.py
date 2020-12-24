# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:30:31 2020

@author: Nishanth

fstm
kanikaim

"""

sent =''' 'Thiruvalluvar' wrote "Thirukkural" '''
print(sent)

s = "First line.\n Second Line"
print(s)


print("Here BackSlach Mistakes")
file_Location = "C:\Progarm Files\new floder"
print(file_Location)

print("Overcome the mistake using r-string")
file_Location = r"C:\Progarm Files\new floder"
print(file_Location)

print("=="*5,"Learn upper()","=="*5)
name="Nisahnth"
print(name.upper())

print("=="*5,"Learn lower()","=="*5)
print(name.lower())

print("=="*5,"Learn title()","=="*5)
news = "prime minster announced schemes for formars"
print(news.title())


print("=="*5,"Learn capitalize()","=="*5)
news = "prime minster announced schemes for formars"
print(news.capitalize())




alphabets='abcdefghijklmnopqrstuvwxyz'
print("Total letter",alphabets)
print("=="*5,"Use +ive ","=="*5)
print("First letter",alphabets[0])
print("Last letter",alphabets[25])

print("=="*5,"Use -ive ","=="*5)
print("Last letter",alphabets[-1])
print("First letter",alphabets[-26])

print("=="*5,"Use bool ","=="*5)
print("First letter",alphabets[False])
print("First letter change Upper",alphabets[False])





print("=="*5,"Learn Slice Operator ","=="*5)
print("First and last index is not necessary")
print("Default start operator is 0")
alphabets='abcdefghijklmnopqrstuvwxyz'
print(alphabets[0:5])
print("First and last index is not necessary")
print(alphabets[5:])
print(alphabets[:5])
print(alphabets[:])

print(alphabets[-1:]) # -1 is last index
print(alphabets[0:-5])
print(alphabets[-5:])

print("Backword slicing is not possiable in python ")
print(alphabets[-1:-3])
print(alphabets[-1:2])

print("=="*5,"Learn Slicing step Operator ","=="*5)
print("Default step operator is 1")
print(alphabets[::2])



Name = "nishanth"
x=Name[0].upper()
y=Name[1:]
print(x+y)

print("Change First Letter In Captial")
print(Name[0].upper() + Name[1:])

print("Change Last Letter In Captial")
print(Name[:-1] + Name[-1].upper())












