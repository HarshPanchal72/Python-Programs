# A program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. 
# If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. 
# If the digit is correct but at the wrong place, the computer should print “Y”. 
# If both the digit and position is correct, the computer should print “R”

import random


code = random.randint(1000, 9999)
code_str = str(code) 
tries = 10

while tries > 0:
    user_guess = input('Enter a four-digit code: ')
    

    if len(user_guess) != 4 or not user_guess.isdigit():
        print('Invalid input. Please enter exactly four digits.')
        continue

    if user_guess == code_str:
        print('R')
        break

    result = ''
    for i in range(4): 
        if user_guess[i] == code_str[i]:
            result += 'R'  
        elif user_guess[i] in code_str:
            result += 'Y'  
        else:
            result += 'B'  
    
    print(result)
    
    tries -= 1  

    if tries == 0:
        print('Sorry, you didn\'t guess the code in time!')
        print('The code was:', code)
