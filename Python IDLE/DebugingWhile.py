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


