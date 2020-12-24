# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:59:46 2020

@author: Nishanth
"""
'''
What are things you known about list ?

        List is a Compound DataType in Python
        List is indicated with []
        List is mutable datatype
        List can contain 'n' of elements
        List can contain Heterogeneous object (elements)

        List can contain duplicate elements
        List maintance insertion order
'''

alpha = ['a','b','c','c']
numeric = [1,2,3,4]
both = [ alpha , numeric ]
print(both)


i = 0
while i < len(alpha):
    print(alpha[i])
    i+=1

x=0 # denote alpha
print(len(both[x]))


box = 0
while box < len(both) : # 0<2 , 0<1, (0<2 -> False)
    item = 0
    while item < len(both[box]): # 0<0 , 0<1 ,0<2 ,0<3 ,(0<4 ->False)
                                # 1<0 , 1<1 ,1<2 ,1<3 ,(1<4 ->False)
        print(both[box][item],end=" ")
        item +=1
    print()
    box+=1




print("Print Alphabate's")
both=str(both)
li = 0
while li < len(both):
    it = 0
    while it < len(both[li]):
        if (both[li][it]).isalpha():
            print(both[li][it],end=" ")
        it +=1
    print()
    li+=1




print("Print Digit's")
li = 0
while li < len(both):
    it = 0
    while it < len(both[li]):
        if (both[li][it]).isdigit():
            print(both[li][it],end="")
        it +=1
    print()
    li+=1



'''

HRNames = []
TestersNames = []
DeveloperNames = []
AdminNames = []
Employee = [[HRNames],[TestersNames],[DeveloperNames],[AdminNames]]

1 Print all names
2 Print only names starting with 'P'



if (type(both[][]) == str):
if (type(both[][]) == int):
'''

alpha = ['a','b','c','c']
numeric = [1,2,3,4]
both = [ alpha , numeric ]
print(both)
c1 = int(input("Enter your first position : "))
c2 = int(input("Enter your first position : "))
S = input("Enter the checking word : ")
for i in range(len(both)):
    for j in range(len(both[i])):
        if i == c1 and j == c2:
            both[i][j] = S
print(both)



print("Remove the list")
alpha = ['a','b','c','c']
numeric = [1,2,3,4]
both = [ alpha , numeric ]
print(both)
alpha.remove('c')
print(both)



number = int(input("Tell us the number : "))
square = []
for i in range(1,number+1):
    square.append(i*i)
print(square)



number = int(input("Tell us the number : "))
square = []
for i in range(1,number+1):
    square.append(i**2)
print(square)






'''

==> Craete Class or method for this,

studentDetails = []
studentCount= int(input("Good Morning Sir,"
                        "Please tell me student count in your class : "))

for student in range(studentCount):
    name,age,percentage = input("Enter your name , age , Percentage separated by space : ").split()
    print("User Details : ",name,age,percentage)

    studentDetails.append(name)
    studentDetails.append(age)
    studentDetails.append(percentage)



count = 1
for data in studentDetails:
    if count%3 == 0: # 3,6,9
        if int(percentage) > 75:
            print(studentDetails[count-3],# 0,3,6
            studentDetails[count-2])# 1,4,7
    count+=1


'''

'''
    1,2,3,4,5,6,7,8,9

        3,6,9
'''













