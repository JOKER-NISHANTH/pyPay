# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:33:02 2020

@author: Nishanth
"""

print("In while print 1 to 10")
no = 1 # Initialising value
while no <= 10: # condition checking 
    print(no,end="")
    no += 1 # increment / decrement
    


'''
    Why we choose for loop instead of while ?
    
    For la increment / decrement and initialisation of values mandatory illaya ?
                 It's coming from c , c ++ , java background guy's
                     syntax :
                         for (int i=0; i<=10;i++)


    I value starts with 0 always is it ?

    We don't have  to initialise it ? 



    In          
        range()  --> function

        In range passing inputs --> arguments / parameters
    
        range(stop) 
        range(start,stop)
        range(start,stop,step)
        
        range is best example for Method(function) overloading
            Same funtion name with different number of arguments [ timestamp 27mins in 11vid ]
        
        stop --> compulsory --> stop - 1
        
        start , stop --> start optional default value is 0
        
        start , stop , step --> start optional default value is 0 and step optional default value is 1


'''



print("\n In for print 1 to 10")
print("\n Default starting value : 0")
print("\n Ending value ( n ) : ( n-1 )")

for no in range(11):
    print(no,end="")

    
for no in range(1,11):
    print(no,end="")    
    
    
    
    
    
print("Addition of 1st 100 numbers") 

total = 0
for i in range(1,101):
    total += i

print("Total of first 100 numbers is ",total)
   
    
    
    
print("Addition of 1st n numbers")         
total = 0
n_number = int(input("Enter any number : "))
for i in range(1,n_number + 1):
    total += i

print(f"Total of first {n_number} numbers is ",total)










for num in range(5,100,10):
    print(num)


for num in range(100,10,-10):
    print(num)
    
for num in range(100,0,-10):
    print(num)
    
    







print("\n  Odd Number in 1 to 100 ")    
for odd in range(1,101):
    if not (odd%2 == 0):
        print(odd , "is Odd")
        
for odd in range(1,101,2):
    print(odd,end=" ")


print("\n  Even Number in 1 to 100 ")    
for even in range(1,101):
    if  (even%2 == 0):
        print(even , "is Even")

for even in range(2,101,2):
    print(even,end=" ")



print("\n  Mulitple of 3 in 1 to 100 ")    
for odd in range(3,101,3):
    print(odd,end=" ")
    
    


start = int(input("Enter the starting value : "))
stop = int(input("Enter the stoping value : "))
step = int(input("Enter the steping value : "))

for i in range(start,stop+1,step):
    print(i)



'''
Palindrome
    eg:
        malayalam - malayalam
        appa      - appa
        amma      - amma
        madam     - madam

'''


word = input("Enter the word to check the word Palindrome or Not : ")

if (word[::-1] == word):
    print(" Palindrome ")

else:
        print(" Not Palindrome ")









Sentence = "God is Great"
for letter in Sentence :
    print(letter,end="")




Sentence = "god is great"
for letter in Sentence :
    if letter in ['a','e','i','o','u']:
        print(letter,end=" ")







Sentence = "love is great"
no_of_space = 0
for letter in Sentence :
    if letter == " ":
        no_of_space += 1
print("No of space in words",no_of_space)






Sentence = "love is great"
no_of_words = 1
for letter in Sentence :
    if letter == " ":
        no_of_words += 1
print("No of  words",no_of_words)







Sentence = "Today is Saturday. Today's Date is 16th"
noOfSentences = 1
for letter in Sentence:
    if letter == '.':
        noOfSentences += 1
print("No of Sentences : ",noOfSentences)        






for letter in range(65,91):
    print(letter,end=" ")


for letter in range(65,91):
    print(chr(letter),end=" ")


for letter in range(ord('A'),ord("Z")+1):
    print(chr(letter),end=" ")


for letter in range(ord('a'),ord("z")+1):
    print(chr(letter),end=" ")
    
    




for num in range(2,10,2):
    pass
    print("Hello",num)
    pass
















    














