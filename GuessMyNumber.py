# Guess My Number
import sys                                      
from random import randint                       
secret_value = randint(1,100)                              
i = 0                                           
print(secret_value)
def gmn(guess_value, secret_value):                                     
    if guess_value == secret_value:                                  
        print('Correct')                        
        sys.exit()                              
    elif secret_value > guess_value:                                 
        print('More')                           
    else:                                       
        print('Less')                           
    return gmn                                  
while i != 10:                                  
    i = i + 1                                    
    guess_value = int(input('Please enter your guess value:')) 
    gmn(guess_value, secret_value)                                      
print('Game Over')                                  
