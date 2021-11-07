#######################################################
## arithmetic.py
## 
## Arithmetic operations trainer.
#######################################################

import random

def addition(x,y):
    '''Returns the sume of two numbers: x and y
    
    Parameters:
    x (int): first number
    y (int): second number

    Returns:
    int: sum of x and y
    '''
    print(f'{x} + {y} = ')
    return x + y

def isint(s):
    '''Checks if string can be converted to int and returns int

    Parameters:
    s (str): string to be checked

    Returns:
    int(s)
    '''

    try:
        s=int(s)
        return s
    except ValueError:
        try:
            s = float(s)
            print(f'{s} is float, not integer.')
        except ValueError:
            print(f'{s} is not a number.')

c = None    # chart in while loop condition

# Loop untill pressing 'q'
while c != 'q':
    x = random.randrange(0,20,1)
    y = random.randrange(0,10,1)

    result = addition(x,y)
    answer = input()

    answer = isint(answer)
    
    ## Check if the answer is correct
    if result == answer:
        print('You are correct!')
    else:
        print('You are wrong...')

    c = input('Press ENTER for next or q to quit: ')
