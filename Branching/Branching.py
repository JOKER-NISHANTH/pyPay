# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:38:43 2020

@author: Nishanth
"""

'''

    if statement should end with            :   True / False
    if needs elif part compulsorily         :   True / False
    if needs else part compulsorily         :   True / False
    elif needs if part compulsorily         :   True / False
    elif needs if part compulsorily         :   True / False

    
    Interpreting Time or Complie Time: 
            .py program --> Byte Code
            
            
    Running Time or RunTime or Execution Time
            Byte Code --> Binary Code
            


function --> Return someData

datatype --> container

type()            

input()  --> str

'''



# Control Statement


print("=="*5," Branching Statement ","=="*5)

mark = int(input("Enter the mark : "))
if mark > 80 :
    print("Excellent")
elif mark > 60 :
    print("Very Good")
else:
    print('Good')



mark1 = int(input("Enter the mark1 : "))
mark2 = int(input("Enter the mark2 : "))
if mark1 == mark2:
    print("Both are same")
elif mark1 > mark2:
    print("mark1 is greater")
else:
    print("mark2 is greater")



'''
    == --> equal to
    
    != --> not equal to 
    
            or
    
    if not Object == "value"
    

'''



age = int(input("Enter your age : "))

if age > 5:
    nationality=input("Enter your nationality : ").lower()
    if nationality == 'indian':
        print("Eligible for Aadhaar Card")
    
    elif not nationality == 'indian':
        print(" Not Eligible for Aadhaar Card")
    
    else:
        print("Not for other nationality")
        pass
else:
    print("Age criteria not met")







print("Sorted function retrun ascending or decending order using ASCII")
word = input("Enter any word : ")
print(sorted((word))     # sorted() --> return list

      
      
word1 = input("Enter any word : ")
word2 = input("Enter any word : ")

'''
eg: 
    vanakkam welcome
    welcome vanakkam
'''

if  sorted(word1) == sorted(word2):
    print("Both are Same")

else:
    print("Not same")
    



mark1 = int(input("Enter your mark : "))
mark2 = int(input("Enter your mark : "))
mark3 = int(input("Enter your mark : "))

if (mark1==mark2) and (mark2==mark3):
    print("All marks are same")

else:
    print('Not same')



















