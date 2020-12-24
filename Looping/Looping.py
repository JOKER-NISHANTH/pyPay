# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:31:51 2020

@author: Nishanth
"""

'''
1 --> Python has a number in its mind

2 --> while your guess does not match with mind value,
please repeat the below steps

3 --> Give your guess(input) as int
'''

mind = 5

match_not_found = True

while match_not_found == True:
#while match_not_found:
#while 1 :
    
    guess = int(input("Enter your guess between 1 to 10 : "))
    
    if guess == mind : 
        
        print(" Your guess is correct ") 
        match_not_found = False
        #break
    
    elif guess > mind : print(" Your guess is higher ")
            
    
    elif guess <  mind : print(" Your guess is lower ")
            
    
    else:
        pass





last = int(input("Enter the number : "))

while last > 0:
    print(last)
    last -=1


last = int(input("Enter the number : "))

while last >= 0:
    print(last)
    last -=1






first=1
last = int(input("Enter the number : "))

while first <= last:
    print(first)
    first += 1


print("=="*5,"Odd number","=="*5)
first=1
last = int(input("Enter the number : "))

while first <= last:
    print(first)
    first += 2


first=2
print("Even number")
last = int(input("Enter the number : "))

while first <= last:
    print(first)
    first += 2





print("=="*5,"print multiple's of 3 b/w 1 to 100","=="*5)
first=3
last = 100
while first <= last:
    print(first)
    first += 3

first = 3
last = 100
while first < last:
    print(first)
    first+=3

first = 1
last = 100
while first <= last:
    if (first%3 == 0):
        print(first)
    first+=1


    

print("=="*5,"print power of 3 b/w 1 to 100","=="*5)
    
    
first=3
last = 100
while first <= last:
    if (first%3 == 0):
        print(first)
        first *= 3

first=3
last = 100
while first <= last:

    print(first)
    first *= 3



print("=="*5,"print div by 2 and 3 b/w 1 to 100","=="*5)

'''
0 --> number = 1
1 --> when the number is less then or equal to 100,
2 --> if the given number is divided by 2 and divided by 3, then 
print the number..
3 --> After this, increment the number by 1.
4 --> Go to step 1
'''

start = 1
end = 100
print("Using nested if ")
while start <=end:
    if start%2==0:
        if start%3==0:
            print(start)
    start +=1



while start <=end:
    if (start%2==0 and start%3==0):
        print(start)
    start+=1

print(" User input the range ")
start,end = input("Enter your range : ").split("-")
start,end=int(start),int(end)
while start <=end:
    if (start%2==0 and start%3==0):
        print(start)
    start+=1
     
    
    
print("=="*5,"print Addition of first ( 100 ) numbers","=="*5)
print("We know to print 1 to 100")

first = 1
last = 100
while first <=100:
    print(first)
    first = first +1
    

first = 1
last = 100
total =0
while first <=100:
    total = total + first 
    first +=1
    
print(total)
    
print("=="*5,"print Multiple of first ( 100 ) numbers","=="*5)

first = 1
last = 100
total = 1
while first <=last:
    total *=first
    first+=1
print(total)






print("=="*5," Learn Break keyword ","=="*5)
print(" Break the statement ")
number = 0
while number < 10:
    number += 1
    if number == 5 :
        break
    print(number)


print("=="*5," Learn Continue keyword ","=="*5)
print(" Continue skip the statement or skip current itration ")
number = 0
while number < 10:
    number += 1
    if number == 5 :
        continue
    print(number)








print("=="*5," print vowels in name ","=="*5)

'''
if word[pre_no] is equal to (a,e,i,o,u) , then print word[pre_no]
'''



print("=="*5," print vowels in name using or operator ","=="*5)

word = input("Enter your name : ").lower()
length = len(word)
pre_no = 0
while pre_no < length:
    if word[pre_no] == 'a' or word[pre_no] == 'e' or word[pre_no] == 'i' or word[pre_no] == 'o' or word[pre_no] == 'u':
        print(word[pre_no])
    pre_no+=1
    
print("Length of word",pre_no)


print("=="*5," print vowels in name using in operator ","=="*5)

word = input("Enter your name : ").lower()
length = len(word)
pre_no = 0
while pre_no < length:
    if word[pre_no] in ['a','e','i','o','u']:
        print(word[pre_no])
    pre_no+=1
    
print("Length of word",pre_no)


print("=="*5," print vowels in name using in and list operator ","=="*5)

word = input("Enter your name : ").lower()
length = len(word)
pre_no = 0
Vowels = ['a','e','i','u','o']
while pre_no < length:
    if word[pre_no] in Vowels:
        print(word[pre_no])
    pre_no+=1
    
print("Length of word",pre_no)







print("=="*5," print no of  vowels in name using in and list operator ","=="*5)

word = input("Enter your name : ").lower()
length = len(word)
pre_no = 0
count = 0
Vowels = ['a','e','i','u','o']
while pre_no < length:
    if word[pre_no] in Vowels:
        print(word[pre_no])
        count += 1
    pre_no+=1
    
print("Length of word",pre_no)

print("No of Vowels in word ",count)      








print("=="*5," Learn else part in while loop this may sure in my knowladge python only accept else in while ","=="*5)  

'''
Real time 
eg:
    ATM pin , only 3 times accept the incorrect pin , more then 3 times , print incorrect go to met the bank manager
    
    
'''

No =1
while No < 5 :
    print(No)
    No+=1
else:
    print("Final NO",No)
    
    
No =1
while No > 5 :
    print(No)
    No+=1
else:
    print("Final NO",No)
    
    
No =1
while No > 5 :
    print(No)
    No+=1
    break

else:
    print("Final NO",No)
    
    
    
    
'''    
name = 'nishanth'    
person = input("What is your name : ")

if name == person:
    print("Please welcome ")
else:
    print("Sorry, you are not the right person ")
    
'''   

name = 'nishanth'    
person = ''

while person != name:
    person = input("Please tell me your name : ").lower()

else:
    print("I got your name ")
    
    
    
name = 'nishanth'    
i = 0
while i < len(name):
    print(name[i] , end="-")
    i+=1
    

name = 'nishanth'    
i = 0
while i < len(name):
    print(name[i] , end=" ")
    i+=1





print("=="*5," Printing multiple of 5 in table format till 10 ","=="*5)  

multiplying_number = 1
number = 5

while multiplying_number <= 10 :
    print(f"{multiplying_number} * {number} = { multiplying_number * number}")
    multiplying_number +=1
    




no_of_subjects = int(input("Please enter no of subject : "))
total = 0
subject_count = 0
while subject_count < no_of_subjects:
    mark = int(input("Enter your mark : "))
    total+=mark
    subject_count += 1
    
print(f"Your total is {total}")




no_of_subjects = int(input("Please enter no of subject : "))
total = 0
subject_count = 0
while subject_count < no_of_subjects:
    mark = int(input("Enter your mark : "))
    total+=mark
    subject_count += 1
    
print(f"Your total is {total}")
print(f"Your precentage is {round(total/no_of_subjects,1)}")












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    